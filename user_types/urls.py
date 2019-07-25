from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view




urlpatterns = [
    path('seller/signup', views.SellerSignupView.as_view(), name='seller_signup'),
    path('buyer/signup', views.BuyerSignupView.as_view(), name='buyer_signup'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('seller/dashboard', views.seller_dashboard, name='seller_dashboard'),
    path('buyer/dashboard', views.buyer_dashboard, name="buyer_dashboard")
]
