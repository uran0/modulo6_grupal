from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('', views.home, name='home'),
    path('perfil/admin/', views.perfil_admin, name='perfil_admin'),
    path('perfil/staff/', views.perfil_staff, name='perfil_staff'),
]