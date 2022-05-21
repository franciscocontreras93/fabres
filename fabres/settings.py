"""
Django settings for fabres project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import os
import dj_database_url
import corsheaders

if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


GEOS_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgeos_c.so' if os.environ.get(
    'ENV') == 'HEROKU' else os.getenv('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgdal.so' if os.environ.get(
    'ENV') == 'HEROKU' else os.getenv('GDAL_LIBRARY_PATH')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-d6!_2(nall^+*0pal+et^%dz@pv&r@j&sh_l&3a%fdnv6xx%g#' # ! CAMBIAR POR VARIABLE DE ENTORNO
SECRET_KEY = os.environ.get('SECRET_KEY','django-insecure-d6!_2(nall^+*0pal+et^%dz@pv&r@j&sh_l&3a%fdnv6xx%g#') # ! CAMBIAR POR VARIABLE DE ENTORNO


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
LOCAL = False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    'rest_framework',
    'widget_tweaks',
    'visor',
    'corsheaders'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fabres.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'visor/templates',
            'templates/dashboard',
            'homepage/templates'
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

WSGI_APPLICATION = 'fabres.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# CASO 1 PRODUCCION REMOTO
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'ec2-3-214-121-14.compute-1.amazonaws.com',
        'PORT': '5432',
        'NAME': 'd6t8mab450ah7e',
        'USER': 'ubaxledfnaqxix',
        'PASSWORD': '705a885bd9edeb6845b17e57f6f4eaaf6e4c19ad31b1636290f808f2fe7dae5a'
    }
}

# if DEBUG == False and LOCAL == False: 
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis',
#             'HOST': 'ec2-3-214-121-14.compute-1.amazonaws.com',
#             'PORT': '5432',
#             'NAME': 'd6t8mab450ah7e',
#             'USER': 'ubaxledfnaqxix',
#             'PASSWORD': '705a885bd9edeb6845b17e57f6f4eaaf6e4c19ad31b1636290f808f2fe7dae5a'
#         }
#     }
# # CASO 2 DEPURACION LOCAL
# elif DEBUG == True and LOCAL == True: 
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis',
#             'HOST': 'localhost',
#             'PORT': '5432',
#             'NAME': 'geodjango',
#             'USER': 'postgres',
#             'PASSWORD': '23826405'
#         }
#     }
# # CASO 3 PRODUCCION LOCAL
# elif DEBUG == False and LOCAL == True:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis',
#             'HOST': 'localhost',
#             'PORT': '5432',
#             'NAME': 'geodjango',
#             'USER': 'postgres',
#             'PASSWORD': '23826405'
#         }

#     }
# # CASO 4 DEPURACION REMOTA
# elif DEBUG == True and LOCAL == False:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis',
#             'HOST': 'ec2-3-214-121-14.compute-1.amazonaws.com',
#             'PORT': '5432',
#             'NAME': 'd6t8mab450ah7e',
#             'USER': 'ubaxledfnaqxix',
#             'PASSWORD': '705a885bd9edeb6845b17e57f6f4eaaf6e4c19ad31b1636290f808f2fe7dae5a'
#         }

#     }



# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# REALIZAR EL COLLECTSTATIC ANTES DE HACER EL DEPLOY
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "visor/static/"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/geoportal/'
LOGOUT_REDIRECT_URL = 'login'

LOGIN_URL = 'login'
