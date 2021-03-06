#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime
import os

AUTHOR = "Naveen Karippai"
SITENAME = "Yellow Elephant"
SITETITLE = "Yellow Elephant in a Green Forest"

# CI server should set SITEURL env var to point to the Domain name
# local dev env should point to localhost
if "SITEURL" in os.environ:
    SITEURL = os.environ['SITEURL']
else:
    SITEURL = "http://localhost:8000"


PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 3
USE_FOLDER_AS_CATEGORY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"

# organize your articles in subfolders
DEFAULT_CATEGORY = 'Travel'

# TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50
NEWEST_FIRST_ARCHIVES = True

LOAD_CONTENT_CACHE = False

STATIC_PATHS = [
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Social widget
SOCIAL = (('github', 'https://github.com/NaveenKarippai'), ('linkedin', 'https://www.linkedin.com/in/naveen-karippai/'))

SHARE_BUTTONS = ('twitter', 'facebook')

# Plugins
PLUGIN_PATHS = ['plugins']
#PLUGINS = ["tag_cloud", "sitemap", "disqus_static"]
PLUGINS = ["tag_cloud", "sitemap"]

# TAG_CLOUD plugin
TAG_CLOUD = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 80
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'random'

# SITEMAP plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Disqus plugin
#DISQUS_SITENAME = 'blog'
#DISQUS_SECRET_KEY = os.environ["DISQUS_SECRET_KEY"]
#DISQUS_PUBLIC_KEY = os.environ["DISQUS_PUBLIC_KEY"]

# Menu
MENUITEMS = (
    ('Categories', '/' + 'categories.html'),
    ('Archive', '/' + 'archives.html'),
)

# Author
AUTHOR_INTRO = "YELLOW ELEPHANT &#9774; Naveen Karippai"
AUTHOR_DESCRIPTION = "Software Engineer from Earth C-137"
AUTHOR_AVATAR = 'https://www.gravatar.com/avatar/abcdefghijkl?s=240'

# Theme customizations
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = datetime.date.today().year
