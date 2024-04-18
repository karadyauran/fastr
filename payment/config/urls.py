from django.contrib import admin
from django.urls import path

import payment.payment_app.views as payment_app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/payment/payment', payment_app.payment, name='payment'),
    path('api/v1/payment/stripe_webhook', payment_app.stripe_webhook, name='stripe_webhook'),
]
