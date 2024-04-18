from django.contrib import admin
from django.urls import path

import user.user_app.views.views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/user_profile',
         user_views.get_user_profile,
         name='user_profile'
         ),

    path('api/v1/delete_user_profile',
         user_views.delete_user_profile,
         name='delete_user_profile'
         ),

    path('api/v1/change_user_profile_image',
         user_views.change_user_profile_image,
         name='change_user_profile_image'
         ),

    path('api/v1/change_user_profile_location',
         user_views.change_user_profile_location,
         name='change_user_profile_location'
         ),

    path('api/v1/change_user_profile_email',
         user_views.change_user_profile_email,
         name='change_user_profile_email'
         ),
]
