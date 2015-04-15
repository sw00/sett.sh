#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from markdown import extensions

AUTHOR = u'Sett Wai'
SITENAME = u'sett.sh'
SITEURL = 'http://sett.sh'
#SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/svbhack'

TAGLINE = 'witty blog tagline here.'
AUTHOR_BIO = 'Code simian, dilettante and functioning absurdist.'
FEED_DOMAIN = 'http://sett.sh'

DISQUS_SITENAME = 'sett-sh'


# Blogroll
LINKS = (('Twitter', 'http://twitter.com/settface'),
         ('Github', 'http://github.com/sw00'),
         ('Keybase', 'http://keybase.io/sw00'))

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
