from settings.base_settings import *

SECRET_KEY = os.environ.get('AUTHENTICATION_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'authenticate_app',
])

AUTH_USER_MODEL = 'authenticate_app.UserAuth'

ROOT_URLCONF = 'authentication.config.urls'
WSGI_APPLICATION = 'authentication.config.wsgi.application'
