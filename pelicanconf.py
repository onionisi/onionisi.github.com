#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chong'
AUTHOR_FULLNAME = 'Chong Yang'
SITENAME = 'TALO'
SITEURL = 'blog.onionisi.com'
SITETAGLINE = 'fprintf(post, "%s\\n", daily_life)'
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = 'en'

MENUITEMS = (
    ('About', '/pages/about.html'),
)

# Theme
THEME = "/home/chong/code/burrito"
EMAIL_ADDRESSS = "iamyangchong@gmail.com"
GITHUB_ADDRESS = "github.com/onionisi"
TWITTER_ADDRESS = "twitter.com/onionisi"

# static
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Plugin
PLUGIN_PATHS = ['/home/chong/code/pelican-plugins']
PLUGINS = ['assets']

# track
GOOGLE_ANALYTICS = "UA-54841037-1"
DISQUS_SITENAME = "chong"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
