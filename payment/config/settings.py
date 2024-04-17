from settings.base_settings import *

SECRET_KEY = os.environ.get('PAYMENT_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([

])

ROOT_URLCONF = 'payment.config.urls'
WSGI_APPLICATION = 'payment.config.wsgi.application'
