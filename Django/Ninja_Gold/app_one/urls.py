from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('farm',views.get_farm),
    path('cave',views.get_cave),
    path('house',views.get_house),
    path('quest',views.get_quest),
    path ('reset', views.reset_gold)
]
