from settings.base_settings import *

SECRET_KEY = os.environ.get('NOTIFICATION_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'notification_app'
])

ROOT_URLCONF = 'notification.config.urls'
WSGI_APPLICATION = 'notification.config.wsgi.application'
