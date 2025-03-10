"""
Django settings for Insportify project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ck(g2(+&@t-o2-mssd@xbx4@+offxrv1o-c&2u-lvts2&1%g+w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['35.182.44.234', '127.0.0.1', 'localhost', 'insportify.com:8000', 'www.insportify.com', '*.insportify.*', 'insportify.com', 'https://localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'widget_tweaks',
    'EventsApp',
    'UserRegister',
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

ROOT_URLCONF = 'Insportify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'UserRegister', 'templates', 'registration')],
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

WSGI_APPLICATION = 'Insportify.wsgi.application'

AUTH_USER_MODEL = 'EventsApp.User'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'insportifyinfo@gmail.com'
EMAIL_HOST_PASSWORD = 'rqhjanxgepfilmrb'


# Added to confirm the csrf token does not fail for Safari on iPhone
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

## Dev DB Configurations

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'insportify',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

## Prod DB Configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Admin2022',
        'HOST': 'insportify3.cz5lufvg1olp.ca-central-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGIN_URL = 'UserRegister:login'
LOGIN_REDIRECT_URL = 'EventsApp:list-events'
LOGOUT_REDIRECT_URL = 'UserRegister:login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240


# TEST Mode
STRIPE_PUBLISHABLE_KEY = 'pk_test_cBzZxJm1Sk4UFJ5i0nypvIEv00HazZHrCi'
STRIPE_SECRET_KEY = 'sk_test_L940ji4j5UAJZm9qmsKICL1Z00Xel3ppet'

# PROD Mode
# STRIPE_PUBLISHABLE_KEY = 'pk_test_cBzZxJm1Sk4UFJ5i0nypvIEv00HazZHrCi'
# STRIPE_SECRET_KEY = 'sk_test_L940ji4j5UAJZm9qmsKICL1Z00Xel3ppet'

