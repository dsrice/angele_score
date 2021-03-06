from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': env('DB_NAME'),
    'USER': env('DB_USER'),
    'PASSWORD': env('DB_PASS'), 
    'HOST': env('DB_HOST'),
    'PORT': env('DB_PORT'),
    'OPTIONS': {
        'charset': 'utf8mb4',
    },
  }
}