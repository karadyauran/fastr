from settings.base_settings import *

SECRET_KEY = os.environ.get('USER_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'user_app',
])

ROOT_URLCONF = 'user.config.urls'
WSGI_APPLICATION = 'user.config.wsgi.application'
