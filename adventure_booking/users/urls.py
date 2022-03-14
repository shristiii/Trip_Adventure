from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('user_home/', views.user_home, name='user_home'),
    path('booking/<str:user>', views.booking, name='booking'),
    path('login/', views.login_page, name='login'),
    path('blog_edit/', views.blog_edit, name='blog_edit'),
    path('view_blog/', views.view_blog, name='view_blog'),
    path('logout', views.logout_page, name='logout'),
    path('blog_edit/<str:user>/<str:pk>', views.blog_edit, name='blog_edit'),
    path('blog_delete/<str:user>/<str:pk>', views.blog_delete, name='blog_delete'),
    path('blog_add/', views.blog_add, name='blog_add'),
    path('all_blog/', views.view_all_blog, name='view_all_blog'),
    # path('accounts/', include('allauth.urls')),
]
