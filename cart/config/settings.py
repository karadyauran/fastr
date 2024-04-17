from settings.base_settings import *

SECRET_KEY = os.environ.get('CART_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([

])

ROOT_URLCONF = 'cart.config.urls'
WSGI_APPLICATION = 'cart.config.wsgi.application'
