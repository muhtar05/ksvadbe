"""
Django settings for ksvadbe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(os.path.expanduser('~'), 'domains/ksvadbe05.ru/static/')
MEDIA_ROOT = os.path.join(os.path.expanduser('~'), 'domains/ksvadbe05.ru/media/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!v2j&u6rs-_vl8j5t@(x^x4k127%@byyczcp(yr5j91q(@cq3m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

YANDEX_MAPS_API_KEY = "AO2k71MBAAAAnOiHJQIAoZ4wB4RXfuRUF45UWYHoIBl29wsAAAAAAAAAAADNWAnhq4OfwhxCWYKiDvIoFT4Y4w=="

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'sorl.thumbnail',
    'imagekit',
    'south',
    'mptt',
    'rest_framework',
    'leaflet',
    'catalog',
    'demo',
    'posts',
    'social_auth',
    'cart',
    #'user-profile',

)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'ksvadbe05.urls'

WSGI_APPLICATION = 'ksvadbe05.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djabrail-92_ksv',  # Or path to database file if using sqlite3.
        'USER': '046014525_ksv',
        'PASSWORD': 'ksvadbe19691961',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # Set to empty string for default.
    }
}

AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID= '298356250332648'
FACEBOOK_API_SECRET= '95f4e34759896309564a4f328ea4911f'
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

VK_APP_ID = '4676543'
VK_API_SECRET = 'R8Tr4swDhAryAjphzXSE'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TEMPLATE_CONTEXT_PROCESSORS = (
#   "social_auth.context_processors.social_auth_by_type_backends"
# )
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook','vk-oauth')

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)