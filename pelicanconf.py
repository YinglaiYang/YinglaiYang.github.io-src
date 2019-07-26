#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yinglai Yang'
SITENAME = u'Yinglai Yang'
TAGLINE = u''
SITEURL = ''

DEV_URL = 'localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = './martin-theme/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (
    ('Home', '{}/index.html'.format(DEV_URL)),
    )

DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('medium', 'https://medium.com/@yinglaiyang'),
          ('linkedin', 'http://www.linkedin.com/in/yinglaiyang'),
          ('twitter', 'https://twitter.com/yinglaiyang'),
          ('github', 'https://github.com/YinglaiYang'),)

DEFAULT_PAGINATION = 7

DEFAULT_METADATA = {
    'status': 'draft',
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
