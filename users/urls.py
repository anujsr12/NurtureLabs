from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "Users" ),
    path('user/login/', views.login, name = "Login"),
    path('user/register/', views.register, name = "Register"),
]