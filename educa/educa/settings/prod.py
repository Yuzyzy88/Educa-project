"""
Custom settings for the production environment
"""
import os
from .base import *

DEBUG = False

ADMINS = [
    ('Antonio M', 'mawarsekali123@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:3679'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]