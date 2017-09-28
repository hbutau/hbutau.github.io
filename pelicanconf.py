#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hamub'
SITENAME = 'djangoindaba'
SITEURL = ''

PATH = 'content'

THEME = 'themes/html5-dopetrope'

LOAD_CONTENT_CACHE = False

TIMEZONE = 'Africa/Harare'

DEFAULT_LANG = 'en'

MENUITEMS = (
    ('Django Indaba', '/'),
    ('Registration', '/registration'),
#    ('Schedule', '/schedule'),
#    ('Sponsorship', '/sponsorship'),
#    ('Call for Proposals', '/call_for_proposals'),
#    ('Volunteering', '/call_for_volunteers'),
    ('CoC', '/coc'),
    ('Recent Developments', '/#developments'),
#    ('About', '/about'),
)

TWITTER_USER = 'django_indaba'
ABOUT_TEXT = 'Whats this all about?'
ABOUT_IMAGE = 'themes/html5-dopetrope/static/images/logo.png'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Django Project', 'https://djangoproject.com'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('twitter', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
