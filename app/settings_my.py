try:
    from app.settings import *
except ImportError, exp:
    pass

DEBUG = True
SECRET_KEY = ''

SOCIAL_AUTH_TWITTER_KEY = 'fNSSzvmyZcaq8Z5aY9Q1HqSk9'
SOCIAL_AUTH_TWITTER_SECRET = 'cRQocZcqef1vtTMRVn4KPkCdEPZNAJf6rlbqoXAdKEwLSRHFPJ'

TWITTER_ACCESS_TOKEN = '54256387-sKGolBCJAgVnpNqHduI8x0YxCuiowgTljW0QvBo6s'
TWITTER_ACCESS_TOKEN_SECRET = '1Dns9yQlE8i4JEiDjNqmwceJ7D1piZmYQgl6lTqNm34cY'

# Uncomment for local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
