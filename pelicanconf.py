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

# Blogroll
LINKS = (('Favorite Song', 'https://www.youtube.com/watch?v=rMnunePFRVU'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./theme"

# organize your articles in subfolders
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'General'

TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50
NEWEST_FIRST_ARCHIVES = True


LOAD_CONTENT_CACHE = False
PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['i18n_subsites']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'cz': {
        'SITENAME': 'Hezkej blog',
	 'THEME' : "./theme/waterspill"
        }
    }

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

