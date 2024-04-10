from django.contrib import admin
from django.urls import path

import auth_app.views as a
import profile_app.views as p

urlpatterns = [
    path('api/v3/admin', admin.site.urls, name='admin'),

    # Authentication
    path('api/v3/signup', a.signup, name='signup'),
    path('api/v3/login', a.login, name='login'),
    path('api/v3/is_stuff', a.is_stuff, name='is_stuff'),
    path('api/v3/get_user', a.get_user, name='get_user'),
    path('api/v3/logout', a.logout, name='logout'),

    # Profile
    path('api/v3/user/get_user_profile', p.get_user_profile, name='get_user_profile'),
    path('api/v3/user/delete', p.delete_user_profile, name='delete_user_profile'),
    path('api/v3/user/location_change', p.change_user_profile_location, name='change_user_profile_location'),
]
