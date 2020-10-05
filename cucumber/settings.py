"""
Django settings for cucumber project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r6*8fuxqn2&xwy&etwingdqt=^zk_!n4hb_dlwnts^_#_w=6k3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'cucumbersports.com', 'cucumbersports.uk.r.appspot.com']


# Application definition

INSTALLED_APPS = [
    'django_jsonforms',
    'crispy_forms',
    'accounts',
    'events',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'cucumber.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'cucumber/templates',
        ],
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

WSGI_APPLICATION = 'cucumber.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cucumber-db-0',
        'USER': 'postgres',
        'PASSWORD': '8M60u8iBLEcB9owF',
        'PORT': '5432',
    }
}
DATABASES['default']['HOST'] = '/cloudsql/cucumbersports:us-east4:cucumbersports-db'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'
    DATABASES['default']['NAME'] = 'cucumber-dev'
    DATABASES['default']['PASSWORD'] = 'a1b1c1d1'
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = 'https://storage.googleapis.com/cucumbersports-static/static/'


# STATIC_ROOT = BASE_DIR / 'staticdeploy'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kinshualternate@gmail.com'
EMAIL_HOST_PASSWORD = 'test@*K9unit'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# MEDIA_ROOT = BASE_DIR / 'media'
# MEDIA_URL = '/media/'

ADMINS = [('Kinshu', 'kinshugupta2002@gmail.com')]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


'''
Upload to gcp bucket
'''

# PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)


# DEFAULT_FILE_STORAGE = 'gcloud.GoogleCloudMediaFileStorage'
# STATICFILES_STORAGE = 'gcloud.GoogleCloudStaticFileStorage'

# GS_PROJECT_ID = 'cucumbersports'
# GS_STATIC_BUCKET_NAME = 'cucumbersports-static'
# GS_MEDIA_BUCKET_NAME = 'cucumbersports-media'  # same as STATIC BUCKET if using single bucket both for static and media

# STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(GS_STATIC_BUCKET_NAME)
# STATIC_ROOT = "static/"
# MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
# MEDIA_ROOT = "media/"

# UPLOAD_ROOT = 'media/'

# DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
# DOWNLOAD_URL = STATIC_URL + "media/downloads"

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'cucumbersports-media'
GS_FILE_OVERWRITE = False