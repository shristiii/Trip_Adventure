
from django.urls import path

from . import views

urlpatterns = [
    path('admin/register/', views.register_page, name='register_page'),
    path('Client_Detail/', views.Client_Detail, name='Client_Detail'),
    path('client_home/', views.client_home, name='client_home'),
    path('trip/', views.trip, name='trip'),
    path('trip/<str:user>/<str:pk>', views.trip, name='trip'),
    path('trip_delete/<str:user>/<str:pk>', views.trip_delete, name='trip_delete'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
]
