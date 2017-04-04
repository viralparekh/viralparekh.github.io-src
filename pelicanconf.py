#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Viral Parekh'
SITENAME = u'Viral Parekh'
SITEURL = ''

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

#pelican-hyde specific
PROFILE_IMAGE='me.jpg'
BIO='Research Scholar @IIIT Hyderabad, Maker , Foodie, Pro Gujarati, Chef & Writer in progress.'
SOCIAL =( ('linkedin','https://www.linkedin.com/in/vparekh1'),
	  ('twitter', 'https://twitter.com/viralmparekh'),
          ('facebook', 'https://facebook.com/viral034'),
          ('github', 'https://github.com/viralparekh'),
          ('quora', 'https://www.quora.com/profile/Viral-Parekh'),
	  ('email','viral@live.in'),)

THEME = 'themes/new-bootstrap2'
NEWEST_FIRST_ARCHIVES = True

