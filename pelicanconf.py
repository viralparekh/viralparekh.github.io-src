#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Viral Parekh'
SITENAME = u'Viral Parekh'
SITEURL = 'https://viralparekh.github.io'
OUTPUT_PATH = '/Users/viral.parekh/work/repos/viralparekh.github.io/'
STATIC_PATHS = ['images', 'pdfs']
PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = '/Users/viral.parekh/work/repos/Portfolio_PelicanHyde/themes/pelican-hyde'
NEWEST_FIRST_ARCHIVES = True

#pelican-hyde specific
PROFILE_IMAGE='me.jpg'
BIO='Data-Scientist at Flipkart, Maker, Foodie.'
SOCIAL =( ('linkedin','https://www.linkedin.com/in/vparekh1'),
	  ('twitter', 'https://twitter.com/viralmparekh'),
          ('facebook', 'https://facebook.com/viral034'),
          ('github', 'https://github.com/viralparekh'),
          ('quora', 'https://www.quora.com/profile/Viral-Parekh'),
	  ('email','viral@live.in'),)

PLUGINS = ['pelican_gist']
