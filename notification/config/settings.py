from settings.base_settings import *

SECRET_KEY = os.environ.get('NOTIFICATION_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([
    'notification_app'
])

ROOT_URLCONF = 'notification.config.urls'
WSGI_APPLICATION = 'notification.config.wsgi.application'
