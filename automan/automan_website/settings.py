"""
Django settings for automan_website project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import datetime
from dotenv import load_dotenv
from os.path import join

dotenv_path = join(os.path.dirname(os.path.abspath(__file__)), '../conf/.env')
load_dotenv(dotenv_path)
sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'middlewares'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "api"))
UPLOAD_FORM_DIRS = os.path.join(BASE_DIR, 'upload_form')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SESSION_COOKIE_DOMAIN = os.environ.get("DOMAIN")
SESSION_COOKIE_NAME = "tier4cookie"
SECRET_KEY = 'g&b45no0o19=r_xdtih8zd+96y_t=!e^)a%1+6=mfv!q$nq5&b'
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'projects',
    'accounts.apps.AccountsConfig',
    'projects.groups',
    'projects.members',
    'projects.calibrations',
    'projects.datasets',
    'projects.annotations',
    'projects.originals',
    'projects.jobs',
    'projects.storages',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.error_handle_middleware.ErrorHandleMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',  # FIXME (for swagger)
        'rest_framework.permissions.AllowAny',           # FIXME (for swagger)
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

ROOT_URLCONF = 'automan_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', os.path.join(UPLOAD_FORM_DIRS, 'templatetags')],
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

WSGI_APPLICATION = 'automan_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DB_NAME"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'HOST': os.environ.get("MYSQL_HOST"),
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../front/dist'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '/',
        'STATS_FILE': os.path.join(BASE_DIR, '../front/webpack-stats.json'),
    }
}

CONN_MAX_AGE = 100

# STORAGE
STORAGE_TYPE = os.environ.get('STORAGE_TYPE')  # Only AZURE
STORAGE_CONFIG = {
    'account_name': os.environ.get('AZURE_STORAGE_ACCOUNT'),
    'account_key': os.environ.get('AZURE_STORAGE_KEY'),
    'container': os.environ.get('AZURE_STORAGE_CONTAINER'),
    'base_uri': 'https://' + os.environ.get('AZURE_STORAGE_ACCOUNT') + '.blob.core.windows.net/'
}

# LOGIN
LOGIN_URL = '/accounts/login/'

# AUTOMAN
AUTOMAN_URL = os.environ.get("AUTOMAN_URL")
AUTOMAN_PORT = os.environ.get("AUTOMAN_PORT")


# SWAGGER
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': None,  # FIXME
    'USE_SESSION_AUTH': False,
}