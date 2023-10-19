from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',  views.home_page, name='home'),
    path('reg_gp/', views.reg_gp, name='reg_gp'),
    path('', views.login_page_gp, name='login_gp'),
    path('login_gp/<str:uid>', views.login_from_uid_gp, name='login_uid_gp'),
    path('logout_gp/', views.logout_page_gp, name='logout_gp'),
    path('reset_gp/', views.reset_view_gp, name='reset_gp'),
    path('reset_gp/<str:uid>', views.reset_from_uid_gp, name='reset_uid_gp'),
]
