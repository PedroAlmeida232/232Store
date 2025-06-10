# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
]
