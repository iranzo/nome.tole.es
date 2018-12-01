# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

AUTHOR = u'No me tolees'
# SITENAME = u"No me tolees!!"
SITENAME =""
# SITESUBTITLE = u'Consejos para lidiar con niños (y no morir en el intento)'
SITEURL = u'/'
TWITTER_USERNAME = ""

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


DEFAULT_CATEGORY = 'general'

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
    'extra/google3bc953001343abe6',
    'image',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/google3bc953001343abe6' : {'path': 'google3bc953001343abe6.html'},
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
THEME = 'themes/nest'

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

LINKS = (('Bebés en amazon', 'https://amzn.to/2DPMZEH'),)

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


# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Inicio', '/'),('Categorías','/categories/'), ('Temas', '/tags/')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/image/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Mapa del sitio'
NEST_SITEMAP_MENU = [('Archivo', '/archives/'),('Etiquetas','/tags/')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Enlaces'
NEST_COPYRIGHT = u'&copy; No me tole.es 2018'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Inicio'
NEST_INDEX_HEADER_TITLE = u'No me tolees!!'
NEST_INDEX_HEADER_SUBTITLE = u"Consejos para lidiar con niños (y no morir en el intento)"
NEST_INDEX_CONTENT_TITLE = u'Últimos artículos'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archivo'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Archivo de entradas'
NEST_ARCHIVES_HEADER_TITLE = u'Archivo'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archivos para todas las entradas'
NEST_ARCHIVES_CONTENT_TITLE = u'Archivo'
# article.html
NEST_ARTICLE_HEADER_BY = u'Por'
NEST_ARTICLE_HEADER_MODIFIED = u'modificado'
NEST_ARTICLE_HEADER_IN = u'en la categoría'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Entradas de '
NEST_AUTHOR_HEAD_DESCRIPTION = u'Entradas de'
NEST_AUTHOR_HEADER_SUBTITLE = u'Archivo de entradas'
NEST_AUTHOR_CONTENT_TITLE = u'Entradas'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Lista de autores'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Lista de autores'
NEST_AUTHORS_HEADER_TITLE = u'Lista de autores'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archivos por autor'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categorías'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archivo por categoría'
NEST_CATEGORIES_HEADER_TITLE = u'Categorías'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archivo ordenado por categoría'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Archivo de categorías'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Archivo de categorías'
NEST_CATEGORY_HEADER_TITLE = u'Categoría'
NEST_CATEGORY_HEADER_SUBTITLE = u'Archivo de categorías'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previo'
NEST_PAGINATION_NEXT = u'Siguiente'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archivo para'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archivo para'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archivo'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archivo para'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archivos para'
# tag.html
NEST_TAG_HEAD_TITLE = u'Archivo de etiquetas'
NEST_TAG_HEAD_DESCRIPTION = u'Archivo de etiquetas'
NEST_TAG_HEADER_TITLE = u'Etiqueta'
NEST_TAG_HEADER_SUBTITLE = u'Archivo de etiquetas'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Etiquetas'
NEST_TAGS_HEAD_DESCRIPTION = u'Listado de etiquetas'
NEST_TAGS_HEADER_TITLE = u'Etiquetas'
NEST_TAGS_HEADER_SUBTITLE = u'Listado de etiquetas'
NEST_TAGS_CONTENT_TITLE = u'Listado de etiquetas'
NEST_TAGS_CONTENT_LIST = u'etiquetado'