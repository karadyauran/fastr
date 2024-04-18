from settings.base_settings import *

SECRET_KEY = os.environ.get('PRODUCT_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([
    'product_app'
])

ROOT_URLCONF = 'product.config.urls'
WSGI_APPLICATION = 'product.config.wsgi.application'
