"""Render equivalent-page language links in HTML, including without JavaScript."""
from copy import copy


def on_page_context(context, *, page, config, nav):
    local_config = copy(config)
    local_config.extra = dict(config.extra)
    local_config.extra['alternate'] = [
        dict(item, link=item['link'] + page.url)
        for item in config.extra['alternate']
    ]
    context['config'] = local_config
    return context
