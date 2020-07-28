from django.urls import path
from home import views

urlpatterns = [
    path('',  views.show_home),
    # path('new', views.show_new)
]