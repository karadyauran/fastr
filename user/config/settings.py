from settings.base_settings import *

SECRET_KEY = os.environ.get('USER_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'user_app',
])

AUTH_USER_MODEL = 'user_app.UserAuth'

ROOT_URLCONF = 'user.config.urls'
WSGI_APPLICATION = 'user.config.wsgi.application'
