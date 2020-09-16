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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} [{asctime}] [{module}.{funcName}:{lineno}] {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/debug.log',
            'when': 'D',
            'interval': 1,
            'formatter': 'verbose',
          },
    },
    'loggers': {
        'django': {
            'handlers': ['console', "file"],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', "file"],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', "file"],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', "file"],
            'level': 'DEBUG',
            'propagate': False,
        },
        'main': {
            'handlers': ['console', "file"],
            'level': 'DEBUG',
        }
    }
}