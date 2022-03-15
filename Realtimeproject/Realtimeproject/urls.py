"""Realtimeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import login_page, register_page, home_page,client_page,clientform_page,booking_page,Description_page,password_page,userlogin_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_page,name="login"),
    path('register/',register_page,name="registration"),
    path('home/',home_page,name="index"),
    path('client/',client_page,name="client"),
    path('clientform/',clientform_page,name="clientform"),
    path('booking/',booking_page,name="Booking"),
    path('Description/',Description_page,name="Description"),
    path('password/',password_page,name="Password"),
    path('userlogin/',userlogin_page,name="userlogin")
]
