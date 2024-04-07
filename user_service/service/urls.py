from django.contrib import admin
from django.urls import path

import auth_app.views as a
import profile_app.views as p

urlpatterns = [
    path('api/v3/admin', admin.site.urls, name='admin'),
    path('api/v3/signup', a.signup, name='signup'),
    path('api/v3/login', a.login, name='login'),
    path('api/v3/test_token', a.test_token, name='test_token'),
    path('api/v3/logout', a.logout, name='logout'),

    path('api/v3/get_user_profile', p.get_user_profile, name='get_user_profile'),
]
