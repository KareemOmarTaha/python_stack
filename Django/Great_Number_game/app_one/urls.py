from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('process', views.calc_rand), 
    path('equal', views.equal_res),
    path ('high' , views.higher),
    path ('low' , views.lower),
    path ('repeat', views.play_again)
]
