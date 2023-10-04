AUTHOR = "Humphrey"
SITENAME = "Hamub"
# SITEURL = "https://hbutau.github.io"

# PORT = 8080
# BIND = "0.0.0.0"

# DISQUS_SITENAME = ""
# GITHUB_URL = "https://github.com/hbutau"
# TWITTER_USERNAME = "hamub"

INDEX_SAVE_AS = "posts.html"
TITLE = "hamub"
BIO = "Blog by Humphrey Butau. Loves open source software programming and 🏃runnning" # noqa
THEME = "themes/pelican-hyde"
COLOR_THEME = "08"
PROFILE_IMAGE = "hamub-pic.jpg"
# PROFILE_IMAGE = ""
STATIC_PATHS = ["images"]

PATH = "content"

TIMEZONE = "Africa/Harare"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (("slides", "https://slides.com"),)

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("envelope", "mailto:hbutau35@gmail.com"),
    ("mastodon", "https://fosstodon.org/@hamub"),
    ("github", "https://github.com/hbutau"),
    ("gitlab", "https://gitlab.com/hbutau"),
    ("stack-overflow", "https://stackoverflow.com/users/5022711/humphrey-butau"), # noqa
)

PYTHON_LINK = '<a href="https://python.org">Python</a>'
PELICAN_LINK = '<a href="https://getpelican.org">Pelican</a>'

FOOTER_TEXT = f"Proudly powerd by {PELICAN_LINK} which takes great advantage of {PYTHON_LINK}"  # noqa

TWITTER_USERNAME = "hamub"

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
