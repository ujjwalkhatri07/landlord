from django.urls import path
from User_login import views


urlpatterns = [
    path('register', views.show_register),
    path('login', views.show_login),
    path('dashboard', views.show_dashboard),
    path('logout', views.do_logout)
]