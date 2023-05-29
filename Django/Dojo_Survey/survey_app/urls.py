from django.urls import path 
from . import views
urlpatterns = [
    path ('' , views.show),
    path ('result' , views.showResult)
]
