#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maru'
SITENAME = "Maru's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"

# organize your articles in subfolders
DEFAULT_CATEGORY = 'General'

TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50
NEWEST_FIRST_ARCHIVES = True

LOAD_CONTENT_CACHE = False

STATIC_PATHS = [
    'extra/robots.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/yourprofile'),
         ('instagram', 'https://instagram.com/yourprofile'),
         ('github', 'https://github.com/yourprofile'))

SHARE_BUTTONS = ('twitter', 'facebook', 'whatsapp', 'mail')
 
# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ["tag_cloud"]

# TAG_CLOUD plugin
TAG_CLOUD = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'
