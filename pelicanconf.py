#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Users Group Nepal'
SITENAME = u'Python Users Group Nepal'
SITETITLE = AUTHOR
TAGLINE = u'#PyNepal'
SITEURL = ''
FAVICON_URL = 'https://www.python.org/static/favicon.ico'
DISPLAY_PAGES_ON_MENU = False


PATH = 'content'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('ILUGC', 'http://ilugc.in/'),
         ('Python', 'http://python.org/'),
         ('PSSI', 'http://python.org.in/'),)

# Social widget
SOCIAL = (('group', 'https://www.meetup.com/PythonNepal/'),
          ('facebook', 'https://www.facebook.com/groups/pythonnepal/'),
          ('rss', 'feeds/all.atom.xml'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "theme"
# COVER_IMG_URL = ""

STATIC_PATHS = ["static"]

MENUITEMS = [
    ("Meetups", "pages/meetups.html")
]

#
# Use the article's filename instead of the article's title for the
# URL. This way conflict due to similar titles can be avoided
#
SLUGIFY_SOURCE = "basename"

CUSTOM_CSS = "static/css/custom.css"
