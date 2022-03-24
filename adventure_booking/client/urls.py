
from django.urls import path

from . import views

urlpatterns = [
    path('admin/register/', views.register_page, name='register_page'),
    path('client_detail/', views.Client_Detail, name='Client_Detail'),
    path('client_home/', views.client_home, name='client_home'),
    path('offer_add/', views.offer_add, name='offer_add'),
    path('offer_edit/<str:user>/<str:pk>', views.offer_edit, name='offer_edit'),
    path('offer_delete/<str:user>/<str:pk>', views.offer_delete, name='offer_delete'),
    path('more_detail/<str:user>/<str:pk>/', views.more_detail, name='more_detail'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
]
