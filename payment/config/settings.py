import os

from settings.base_settings import *

SECRET_KEY = os.environ.get('PAYMENT_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([
    'payment_app'
])

ROOT_URLCONF = 'payment.config.urls'
WSGI_APPLICATION = 'payment.config.wsgi.application'

STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')
STRIPE_TEST_SECRET_KEY = os.getenv('STRIPE_TEST_SECRET_KEY')
STRIPE_LIVE_MODE = False  # Test, for production True
