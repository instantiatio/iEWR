"""Equivalent-page links and presentation of the accepted Blue Architecture style."""
from copy import copy
import hashlib
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup


def on_config(config):
    digest = hashlib.sha256((Path(__file__).parent / 'assets/site.css').read_bytes()).hexdigest()[:12]
    config.extra_css = [value + '?v=' + digest if value == '/iEWR/assets/site.css' else value
                        for value in config.extra_css]
    return config


def on_page_content(html, *, page, config, files):
    if not page.is_homepage:
        return html
    doc = BeautifulSoup(html, 'html.parser')
    nodes = list(doc.contents)
    cut = next(i for i, node in enumerate(nodes) if getattr(node, 'name', None) == 'h2')
    intro = BeautifulSoup(''.join(str(x) for x in nodes[:cut]), 'html.parser')
    heading = intro.h1.extract()
    permalink = heading.select_one('.headerlink')
    if permalink:
        permalink.extract()
    heading.clear()
    heading.append('AI-native-first')
    heading.append(intro.new_tag('br'))
    engineering = intro.new_tag('span')
    engineering.string = 'engineering' if config.theme['language'] == 'en' else 'инженерия'
    heading.append(engineering)
    if permalink:
        heading.append(permalink)
    paras = intro.find_all('p', recursive=False)
    actions = paras[-1].extract(); actions['class'] = ['hero-actions']
    body = ''.join(str(p) for p in paras[:-1])
    label = ('Instantiatio / Research programme' if config.theme['language'] == 'en'
             else 'Instantiatio / Исследовательская программа')
    hero = f'''<section class="hero"><div class="container hero-inner">
<p class="eyebrow">{label}</p><div class="hero-heading">{heading}</div>
<div class="hero-support"><div class="hero-copy">{body}</div>{actions}</div>
</div></section>'''
    rest = BeautifulSoup(''.join(str(x) for x in nodes[cut:]), 'html.parser')
    sections, current = [], None
    for node in list(rest.contents):
        if getattr(node, 'name', None) == 'h2':
            current = rest.new_tag('section', attrs={'class': 'home-section'})
            sections.append(current)
            number = rest.new_tag('span', attrs={'class': 'section-number', 'aria-hidden': 'true'})
            number.string = f'{len(sections):02d}'
            head = rest.new_tag('div', attrs={'class': 'section-heading'})
            head.append(number); head.append(node.extract()); current.append(head)
            current.append(rest.new_tag('div', attrs={'class': 'section-body'}))
        elif current is not None:
            current.select_one('.section-body').append(node.extract())
    for section in sections:
        images = section.find_all('img')
        if images:
            section['class'].append('case-section')
            strip = rest.new_tag('div', attrs={'class': 'case-images'})
            for image in images:
                image['loading'] = 'lazy'
                image['width'], image['height'] = '1600', '1000'
                strip.append(image.parent.extract())
            section.select_one('.section-body').find('p', recursive=False).insert_after(strip)
    return hero + '<div class="container home-body">' + ''.join(str(s) for s in sections) + '</div>'


def on_page_context(context, *, page, config, nav):
    local_config = copy(config)
    local_config.extra = dict(config.extra)
    local_config.extra['alternate'] = [
        dict(item, link=item['link'] + page.url)
        for item in config.extra['alternate']
    ]
    context['config'] = local_config
    locale = 'eng' if config.theme['language'] == 'en' else 'ru'
    context['locale'] = locale
    context['locale_root'] = urlsplit(config.site_url).path
    context['site_navigation'] = [
        {'title': item.title, 'url': item.children[0].url if item.is_section else item.url,
         'active': item.active}
        for item in nav.items
    ]
    context['foundation_navigation'] = [
        child for item in nav.items if item.is_section and item.children[0].url == 'foundations/'
        for child in item.children[1:]
    ]
    content = BeautifulSoup(page.content, 'html.parser')
    context['content_sections'] = [
        {'title': heading.get_text(' ', strip=True).removesuffix('¶').strip(), 'id': heading.get('id')}
        for heading in content.find_all('h2')
    ]
    return context
