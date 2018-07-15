#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Alex Fitts'
SITENAME = u'Alex Fitts'
SITEURL = 'http://afitts.github.io'#'http://www.gregreda.com'
TIMEZONE = 'America/Chicago'
THEME = 'void/'
AVATAR = '/theme/images/avatar.jpg'
TITLE = "Alex Fitts: independent data science and strategy consulting."
DESCRIPTION = "Alex Fitts is a curious astronomy who has wandered into \
the world of data science. What started out as a way to better understand\
astronomy has taken a life of its own."

# TODO: switch to /blog/slug/index.html -- need to setup redirects first
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = 'Per aspera ad astra.'

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', 'pelican_dynamic']
PLUGINS = ['assets', 'liquid_tags.notebook', 'pelican_dynamic', 'render_math']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = ['images', 'code', 'notebooks', 'extra', 'data']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}

# TODO: NAVBAR - make it dynamic
NAVIGATION = [
    (),
]

# TODO: SOCIAL - make it dynamic
TWITTER_CARDS = True
TWITTER_NAME = "Alex_Fitts"
FACEBOOK_SHARE = True
GITHUB_NAME = 'afitts'
LINKEDIN_URL = 'https://www.linkedin.com/in/alex-fitts-64163b128/'
GOOGLE_PLUS_URL = 'https://plus.google.com/u/0/117088506946894057793/about/p/pub'
LASTFM_NAME = 'gjreda'

#### Analytics
GOOGLE_ANALYTICS = 'UA-34295039-1'
DOMAIN = "gregreda.com"

# Other
MAILCHIMP = False
CACHE_CONTENT = False
AUTORELOAD_IGNORE_CACHE = True
