
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path ('create' , views.Add_dojo),
    path ('add', views.add_ninja)
]
