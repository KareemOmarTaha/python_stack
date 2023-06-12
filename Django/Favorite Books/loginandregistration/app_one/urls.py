from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),	
    path('books', views.view_book),	
    path('login', views.login),	
    path('logout', views.logout),
    path('createbook', views.create_book),
    path('addFav/<int:ID>' , views.add_favorite),
    path('books/<int:num>' , views.show_details),
    path('removeFav/<int:ID>',views.remove_favorite),
    path ('updated/<int:num>' , views.updated_book),
    path ('delete/<int:num>' , views.delete_book),
]
