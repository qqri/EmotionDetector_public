"""
Django settings for boardsite project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7pid)7*h(wpspmwr8-6amfca8q_!rw!)mm1$%f-p5b1ocr094x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'haystack',
    'elasticsearch',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boardsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'boardsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MODEL_URL = '/model/'
MODEL_ROOT = os.path.join(BASE_DIR, 'static' ,'model/gru_model.pkl')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGE_SIZE': 10
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch5_backend.Elasticsearch5SearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

ELASTICSEARCH_DEFAULT_ANALYZER = 'korean_index'


ELASTICSEARCH_INDEX_SETTINGS = {
  'settings': {
      "analysis": {
          "analyzer": {
              "korean_index": {
                  "type": "custom",
                  "tokenizer": "mecab_ko_standard_tokenizer"
              },
              "korean_query": {
                  "type": "custom",
                  "tokenizer": "korean_query_tokenizer"
              },
              "ngram_analyzer": {
                  "type": "custom",
                  "tokenizer": "standard",
                  "filter": ["haystack_ngram", "lowercase"]
              },
              "edgengram_analyzer": {
                  "type": "custom",
                  "tokenizer": "standard",
                  "filter": ["haystack_edgengram", "lowercase"]
              }
          },
          "tokenizer": {
              "korean_query_tokenizer": {
                  "type": "mecab_ko_standard_tokenizer",
                  "compound_noun_min_length": 100
              },
              "haystack_ngram_tokenizer": {
                  "type": "nGram",
                  "min_gram": 3,
                  "max_gram": 15,
              },
              "haystack_edgengram_tokenizer": {
                  "type": "edgeNGram",
                  "min_gram": 2,
                  "max_gram": 15,
                  "side": "front"
              }
          },
          "filter": {
              "haystack_ngram": {
                  "type": "nGram",
                  "min_gram": 3,
                  "max_gram": 15
              },
              "haystack_edgengram": {
                  "type": "edgeNGram",
                  "min_gram": 2,
                  "max_gram": 15
              }
          }
      }
  }
}







