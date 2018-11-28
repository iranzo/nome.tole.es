# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

AUTHOR = u'No me tolees'
SITENAME = u"¿Este niño no tiene manual?"
SITESUBTITLE = u'Consejos para lidiar con ellos (y no morir en el intento)'
SITEURL = u'/'
TWITTER_USERNAME = ""
# https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
MAIN_MENU = False

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

# Put as draft content in the future
WITH_FUTURE_DATES = True

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Default theme language.
I18N_TEMPLATES_LANG = 'es'

DEFAULT_LANG = 'es'
OG_LOCALE = 'es_ES'
LOCALE = 'es_ES'

# I18N_SUBSITES = {
#     'es': {
#         'SITENAME': 'No me tole.ES',
#         }
#     }


DEFAULT_CATEGORY = 'blog'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
TRANSLATION_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_RSS = 'feeds/%s.rss'
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss'
TAG_FEED_ATOM = 'feeds/tag_%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag_%s.rss'

DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = [
    'imagen',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/google3bc953001343abe6'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/google3bc953001343abe6' : {'path': 'google3bc953001343abe6.html'}
}

CACHE_CONTENT = False
CACHE_PATH = '.cache'
LOAD_CONTENT_CACHE = False

# Plugins
PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'better_codeblock_line_numbering',
    'better_figures_and_images',
    'sitemap',
    # 'yuicompressor',
    'i18n_subsites',
    "representative_image",
    "related_posts",
]

# Enable i18n plugin, probably you already have some others here.
# PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

FAVICON = 'extra/favicon.ico'
THEME = 'themes/Flex'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False


# URL Settings to be compatible with octopress
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'

YEAR_ARCHIVE_URL = 'blog/archive/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'blog/archive/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = 'blog/archive/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'blog/archive/{date:%Y}/{date:%m}/index.html'

CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'

TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = 'blog/author/{slug}/'
AUTHORS_SAVE_AS = 'blog/authors/{slug}/'

ARCHIVES_URL = 'blog/archives/'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

CATEGORIES_URL = 'blog/categories/'
CATEGORIES_SAVE_AS = 'blog/categories/index.html'

TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']

LINKS = ()

# SOCIAL = (('telegram', 'https://t.me/nometolees'),)
SOCIAL = ()

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# better codeblock
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': False},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# sitemap
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

SITE_UPDATED = datetime.date.today()

GOOGLE_ANALYTICS = "UA-81705-15"


# blue-penguin

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'
AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

DISQUS_SITENAME = "nome-tole-es"
DISQUS_DISPLAY_COUNTS = True
