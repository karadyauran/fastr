from django.contrib import admin
from django.urls import path

import authentication.authenticate.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
]
