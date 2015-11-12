"""
Django settings for platal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import getconf
CONFIG = getconf.ConfigGetter('platal', [os.path.join(BASE_DIR, 'local_settings.ini')])

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('django.secret_key', 'Dev only!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

AUTH_USER_MODEL = 'auth.Account'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'platal.auth',
    'platal.profiles',
    'corsheaders',
    'rest_framework',
)

AUTHENTICATION_BACKENDS = [
    'platal.auth.backends.PlatalAuthBackend',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'platal1': {
        'ENGINE': 'django.db.backends.' + CONFIG.get('plataldb.engine', 'sqlite3'),
        'NAME': CONFIG.get('plataldb.name', 'x5dat'),
        'USER': CONFIG.get('plataldb.user', 'web'),
        'PASSWORD': CONFIG.get('plataldb.password'),
        'HOST': CONFIG.get('plataldb.host', '127.0.0.1'),
        'PORT': CONFIG.get('plataldb.port', '3306'),
    },
}

# Do not manage MySQL databases but manage SQLite ones for tests and local development
PLATAL_MANAGED = (DATABASES['platal1']['ENGINE'] == 'django.db.backends.sqlite3')

DATABASE_ROUTERS = ['backend.dbrouter.SimpleRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Enabled Cross-Origin requests from http://localhost:8000/.
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)
# Tell the browser he is allowed to send cookies.
# FIXME(rbarrois): This should disappear once we use tokens.
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
    'PAGINATE_BY': 20,
}
