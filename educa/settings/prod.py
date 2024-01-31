"""
Custom settings for the production environment
"""
from .base import *

DEBUG = False

ADMINS = [
    ('Antonio M', 'mawarsekali123@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {

    }
}