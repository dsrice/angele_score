from .base import *
import environ

env = environ.Env()
env.read_env('.env')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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