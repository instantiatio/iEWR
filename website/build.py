"""Build both MkDocs projects and the shared GitHub Pages root."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def main():
    with tempfile.TemporaryDirectory(prefix='iewr-site-') as tmp:
        stage = Path(tmp)
        for locale in ('eng', 'ru'):
            subprocess.run([
                sys.executable, '-m', 'mkdocs', 'build', '--strict', '--quiet',
                '--config-file', str(ROOT / f'mkdocs.{locale}.yml'),
                '--site-dir', str(stage / locale),
            ], check=True, cwd=ROOT)
        shutil.copytree(ROOT / 'assets', stage / 'assets')
        (stage / '.nojekyll').touch()
        (stage / 'index.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Instantiatio / iEWR</title>
<link rel="canonical" href="https://instantiatio.github.io/iEWR/eng/">
<meta http-equiv="refresh" content="0; url=eng/">
</head><body><p><a href="eng/">Continue in English</a> · <a href="ru/">Русский</a></p>
<script>location.replace(new URL("eng/", location.href).href);</script>
</body></html>''', encoding='utf-8')
        (stage / '404.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found / Страница не найдена — Instantiatio</title></head>
<body><h1>Page not found / Страница не найдена</h1>
<p><a href="/iEWR/eng/">Home</a> · <a href="/iEWR/ru/">Главная</a></p></body></html>''', encoding='utf-8')
        (stage / 'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<sitemap><loc>https://instantiatio.github.io/iEWR/eng/sitemap.xml</loc></sitemap>
<sitemap><loc>https://instantiatio.github.io/iEWR/ru/sitemap.xml</loc></sitemap>
</sitemapindex>''', encoding='utf-8')
        output = ROOT / 'site'
        if output.exists():
            shutil.rmtree(output)
        shutil.copytree(stage, output)
        print(f'Built {output}')


if __name__ == '__main__':
    main()
