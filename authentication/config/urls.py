from django.contrib import admin
from django.urls import path

import authentication.authenticate.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_auth'),

    path('api/v1/login', auth_views.login, name='login'),
    path('api/v1/signup', auth_views.signup, name='signup'),
    path('api/v1/logout', auth_views.logout, name='logout'),
]
