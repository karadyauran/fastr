from settings.base_settings import *

SECRET_KEY = os.environ.get('ORDER_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'order_app'
])

ROOT_URLCONF = 'order.config.urls'
WSGI_APPLICATION = 'order.config.wsgi.application'
