from pathlib import Path
from settings.base_settings import *

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('CART_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.extend([

])

ROOT_URLCONF = 'cart.config.urls'
