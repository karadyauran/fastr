from settings.base_settings import *

SECRET_KEY = os.environ.get('CART_SECRET_KEY')
DEBUG = True

INSTALLED_APPS.extend([
    'cart_app',
])

ROOT_URLCONF = 'cart.config.urls'
WSGI_APPLICATION = 'cart.config.wsgi.application'
