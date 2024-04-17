from pathlib import Path
from settings.base_settings import *

# BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('ORDER_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([

])

ROOT_URLCONF = 'order.config.urls'
WSGI_APPLICATION = 'order.config.wsgi.application'
