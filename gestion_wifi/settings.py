"""
Django settings for gestion_wifi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RUTA_TEMPLATES = os.path.join(BASE_DIR, 'templates')
RUTA_HTML = os.path.join(BASE_DIR, 'html')
# Ruta de las imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'foto')
MEDIA_URL = '/foto/'

# Reporte
MEDIA_PDF = os.path.join(BASE_DIR, 'reporte')
REPORTE = '/reporte/'

TEMPLATE_DIRS = (RUTA_TEMPLATES, RUTA_HTML,)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e6tzjw)*7&6i6pxp7gfmhj)5o5jy!ev1dek!76uqxxxa5q0-*0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pixelfields_smart_selects',
    'django_extensions',
    'apps.cantidad_usuario',
    'apps.grafica',# modelo de registro de cantidad de usuarios WIFI
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gestion_wifi.urls'

WSGI_APPLICATION = 'gestion_wifi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

USER = "SIRSEA"
PASSWORD = "S1RS34J3"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gestion_wifi',
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home/administrador/django/gestion_wifi/static/'
STATIC_URL ='http://gestionwifi.bva.org.ve/static/'
#STATIC_URL = '/static/'


RUTA_STATIC = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (RUTA_STATIC,)

# Cierre de session de forma automatica al cerrar el navegador
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_NAME = 'gestion_wifi'
