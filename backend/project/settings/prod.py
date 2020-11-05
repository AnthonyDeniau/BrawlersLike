import os
import json
from .base import *
import logging.config

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = os.getenv('DEBUG', "False") == "True"
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'brawler_db'),
        'USER': os.getenv('POSTGRES_USER', 'brawler_dbusr'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', 5432),
        'OPTIONS': json.loads(os.getenv('DATABASE_OPTIONS', '{}')),
    }
}

# Logging Configuration

# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format':
            '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': [
                'console',
            ],
        },
    },
})

SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME', "brawlerlike")
STATIC_URL = "/django/static/"
STATIC_ROOT = "/data/www/django/static"
MEDIA_URL = "/django/media/"
MEDIA_ROOT = "/data/www/django/media"

INSTALLED_APPS += ['django_prometheus']
MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware', *MIDDLEWARE,
    'django_prometheus.middleware.PrometheusAfterMiddleware'
]
PROMETHEUS_EXPORT_MIGRATIONS = False