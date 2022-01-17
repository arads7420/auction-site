"""
Django settings for auctionsite project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+di)xr=gjqb$v^m)e)dm%lqmxn@o7#697e0_l(%4x%=&45v_kw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['auction-house-01.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'auctions.apps.AuctionsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'currencies',
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auctionsite.urls'

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
                'currencies.context_processors.currencies',
                'auctions.views.category_list'
            ],
        },
    },
]

WSGI_APPLICATION = 'auctionsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db535614agn24s',
        'USER': 'zsfpjvgfqhdeht',
        'PASSWORD': 'da26fc42189c608dcca75ed0eb1109b06050c42231de881a25e44db8fb814616',
        'HOST': 'ec2-52-1-20-236.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

CLOUDINARY_STORAGE = {
             'CLOUD_NAME': 'auction-house-images',
             'API_KEY': '387944874292187',
             'API_SECRET': '9yl3OSpIU00i6nqeoiIH50cVFUs'
            }

DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

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

DEFAULT_CURRENCY = 'INR'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'auctions/static/auctions/')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Stripe Settings
STRIPE_PUBLISHABLE_KEY = "pk_test_51JLNKrSFuC5f8eVLhWtJXfGXooMMVNfwhAnnnXXCqWKTAttAyLYUN1vOHhFpfNS8ewSProY7ktb4xFxhcq1Ox26T00ck8mRFgO"
STRIPE_SECRET_KEY = "sk_test_51JLNKrSFuC5f8eVLn1KgmJgBB1XYAOUpvstt4evvUtZG9hex5LvdyS2nFj9LrggNyd4BGGGfXSp4LFD0JEMPD7Ck00ehvbywha"
STRIPE_WEBHOOK_SECRET = ""
STRIPE_CONNECT_CLIENT_ID = 'ca_JzM6GsjmulrvWzCmVYKDi53p3IWv3M4K'
