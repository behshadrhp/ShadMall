import os

from .common import *

import dj_database_url

from dotenv import load_dotenv

# Loading environment variable's
load_dotenv()

# Django secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Enable sever mode
DEBUG = False

# Allowed run server in this host
FIRST_HOST = os.environ.get('FIRST_HOST')
SECOND_HOST = os.environ.get('SECOND_HOST')

ALLOWED_HOSTS = ['127.0.0.1', FIRST_HOST, SECOND_HOST]

# Final database
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL')),
}


# Configure Cache system
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 # 7 Days
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# CSRF Attack
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# XSS Attack
SECURE_BROWSER_XSS_FILTER = True
SECURE_COUNT_TYPE_NOSNIFF = True

# CORS Origin Header settings configuration
CORS_ORIGIN = os.environ.get('CORS_ORIGIN')
CSRF_ORIGINS = os.environ.get('CSRF_ORIGINS')
CORS_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS')
CORS_ALLOW_CREDENTIALS = os.environ.get('CORS_ALLOW_CREDENTIALS')
CORS_ALLOWED_ORIGINS = [CORS_ORIGIN]
CSRF_TRUSTED_ORIGINS = [CSRF_ORIGINS]
CORS_ALLOW_ALL_ORIGINS = CORS_ALL_ORIGINS
