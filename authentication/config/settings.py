from settings.base_settings import *

SECRET_KEY = os.environ.get('AUTHENTICATION_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([

])

ROOT_URLCONF = 'authentication.config.urls'
WSGI_APPLICATION = 'authentication.config.wsgi.application'
