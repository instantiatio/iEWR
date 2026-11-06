"""Check the built project URLs, locale pairs, search, links and evidence."""
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import hashlib
import json
import re
import sys
import zipfile

from bs4 import BeautifulSoup
import markdown

ROOT = Path(__file__).resolve().parent
BASE = 'https://instantiatio.github.io/iEWR/'
PATHS = ('', 'try/', 'try/advanced/', 'try/first-experiment/', 'applications/', 'cases/', 'cases/geo-crm/', 'cases/quotation-expiry/', 'foundations/',
         'foundations/instantiatio/', 'foundations/ai-native-first/',
         'foundations/system-formation/', 'foundations/ewr/',
         'foundations/methods/', 'how-iewr-works/', 'about/')
PRIVATE = re.compile(r'/Users/[^\s<]+|/home/[^\s<]+|/private/(?:tmp|var)/[^\s<]+'
                     r'|(?:github_pat_|ghp_|sk-proj-)[A-Za-z0-9_\-]+')


def check(site):
    errors, external = [], set()
    documents = {}
    for file in site.rglob('*.html'):
        documents[file] = BeautifulSoup(file.read_text(), 'html.parser')
    for file, doc in documents.items():
        url = BASE + file.relative_to(site).as_posix().removesuffix('index.html')
        for node in doc.select('[href], img[src], script[src]'):
            ref = node.get('href', node.get('src', ''))
            resolved = urlsplit(urljoin(url, ref))
            if resolved.scheme not in ('http', 'https'):
                continue
            if resolved.netloc.lower() in ('t.me', 'www.t.me', 'telegram.me', 'telegram.org'):
                errors.append(f'{file}: Telegram link: {ref}')
            if resolved.netloc != urlsplit(BASE).netloc:
                external.add(resolved._replace(fragment='').geturl())
                continue
            if not resolved.path.startswith('/iEWR/'):
                errors.append(f'{file}: URL escapes project: {ref}')
                continue
            target = site / unquote(resolved.path.removeprefix('/iEWR/'))
            if resolved.path.endswith('/'):
                target = target / 'index.html'
            if not target.is_file():
                errors.append(f'{file}: missing {ref}')
            elif resolved.fragment and target.suffix == '.html':
                target_doc = documents.get(target)
                if target_doc and not target_doc.find(id=unquote(resolved.fragment)):
                    errors.append(f'{file}: missing anchor {ref}')
        for img in doc.select('article img'):
            if not img.get('alt'):
                errors.append(f'{file}: image without alt text')
    for locale, code in (('eng', 'en'), ('ru', 'ru')):
        for path in PATHS:
            file = site / locale / path / 'index.html'
            doc = documents.get(file)
            if doc is None:
                errors.append(f'missing page {locale}/{path}')
                continue
            expected = BASE + locale + '/' + path
            analytics = doc.select('script[src="https://plausible.io/js/pa-BakopUlN_Wa9Gy2RmlLyO.js"]')
            if len(analytics) != 1 or not analytics[0].has_attr('async'):
                errors.append(f'{file}: missing, duplicate or blocking Plausible script')
            if sum('plausible.init()' in script.get_text() for script in doc.find_all('script')) != 1:
                errors.append(f'{file}: Plausible must initialize exactly once')
            if path == 'cases/geo-crm/' and any(
                    urlsplit(a['href']).path.lower().endswith('.zip')
                    for a in doc.select('article a[href]')):
                errors.append(f'{file}: GEO CRM evidence must be PDF, not ZIP')
            if doc.html.get('lang') != code:
                errors.append(f'{file}: wrong HTML language')
            source = ROOT / 'docs' / locale / path / 'index.md'
            text = re.sub(r'^---\n.*?\n---\n', '', source.read_text(), count=1, flags=re.S)
            original = BeautifulSoup(markdown.markdown(text, extensions=['attr_list', 'tables', 'fenced_code', 'toc']), 'html.parser')
            article = BeautifulSoup(str(doc.select_one('.md-content article')), 'html.parser')
            if path.startswith('try/') and 'Codex CLI' in article.get_text():
                errors.append(f'{file}: terminal-specific Codex route in Try')
            for added in article.select('.eyebrow, .section-number, .headerlink'):
                added.decompose()
            tokenize = lambda value: re.findall(r'\w+|[^\w\s]', value, flags=re.UNICODE)
            if tokenize(original.get_text(' ', strip=True)) != tokenize(article.get_text(' ', strip=True)):
                errors.append(f'{file}: presentation changed content or its order')
            if not any(urlsplit(urljoin(expected, link.get('href', ''))).path == f'/iEWR/{locale}/how-iewr-works/'
                       for link in doc.select('header .desktop-nav a')):
                errors.append(f'{file}: How iEWR works missing from main navigation')
            if not doc.select_one('header .site-search-button') or not doc.select_one('.md-search[data-md-component="search"]'):
                errors.append(f'{file}: missing native search')
            if not doc.select_one('header .site-menu-button[for="__drawer"]'):
                errors.append(f'{file}: missing native mobile menu')
            if (site / locale / path / 'sitemap.xml').read_bytes() != (site / locale / 'sitemap.xml').read_bytes():
                errors.append(f'{file}: translation sitemap discovery differs from locale sitemap')
            canonical = doc.find('link', rel='canonical')
            if not canonical or canonical.get('href') != expected:
                errors.append(f'{file}: wrong canonical')
            for other, other_code in (('eng', 'en'), ('ru', 'ru')):
                link = doc.select_one(f'.md-select__link[hreflang="{other_code}"]')
                if not link or link.get('href') != '/iEWR/' + other + '/' + path:
                    errors.append(f'{file}: language switch loses page')
        search = json.loads((site / locale / 'search/search_index.json').read_text())
        found = {urlsplit(x['location']).path for x in search['docs']}
        for path in PATHS:
            if path not in found:
                errors.append(f'{locale}: missing search document {path}')
        if search['config']['lang'] != [code]:
            errors.append(f'{locale}: wrong search language')
    root = documents[site / 'index.html']
    redirect = root.find('meta', attrs={'http-equiv': 'refresh'})
    if not redirect or redirect.get('content') != '0; url=eng/':
        errors.append('root does not redirect to English')
    for file in site.rglob('*'):
        if file.suffix in ('.html', '.json', '.xml', '.txt', '.css', '.js'):
            if PRIVATE.search(file.read_text()):
                errors.append(f'{file}: private path or token pattern')
        elif file.suffix == '.zip':
            with zipfile.ZipFile(file) as z:
                if z.testzip():
                    errors.append(f'{file}: failed ZIP CRC')
                for name in z.namelist():
                    if name.startswith('/') or '..' in Path(name).parts:
                        errors.append(f'{file}: unsafe ZIP member {name}')
                    if name.endswith(('.md', '.txt', '.json', '.xml', '.csv', '.py')):
                        if PRIVATE.search(z.read(name).decode('utf-8')):
                            errors.append(f'{file}: private path or token in {name}')
    if (site / 'assets/geo-crm-evidence.zip').exists():
        errors.append('GEO CRM evidence ZIP must not be published')
    manifest = json.loads((ROOT / 'evidence-manifest.json').read_text())
    for relative, digest in manifest.items():
        file = site / relative
        if hashlib.sha256(file.read_bytes()).hexdigest() != digest:
            errors.append(f'{relative}: evidence bytes changed')
    return {'pages': 2 * len(PATHS), 'html_documents': len(documents),
            'evidence_files': len(manifest), 'errors': errors,
            'external_urls': sorted(external)}


if __name__ == '__main__':
    result = check(ROOT / 'site')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result['errors']))
