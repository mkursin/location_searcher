# coding=utf-8

"""
Django settings for location project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#GEOIP_PATH = ("/usr/local/lib/python2.7/dist-packages/django/contrib/gis/geoip", 'geoip')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY='f^@*w2scsui0k)ci5xdi87urh6)w_x9z!c)zr+-*pay9$u&y28'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CELERY_REDIS_HOST = '127.0.0.1'
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0
CELERY_RESULT_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379/0'

REDIS_CONNECT_RETRY = True
CELERY_IGNORE_RESULT = False
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = 60


import djcelery
djcelery.setup_loader()

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'location',
    'LocationsByIp',
    "djcelery",

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

)


ROOT_URLCONF = 'location.urls'

WSGI_APPLICATION = 'location.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'locations',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
