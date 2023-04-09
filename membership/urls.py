# membership/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.membership_payment, name='membership_payment'),
    path('success/', views.membership_success, name='membership_success'),
]
