from django.shortcuts import render , redirect
from . import models
def index (request):
    context = {
        "dojo_name" : models.show_dojos(),
        "ninja_name" : models.show_ninja(),
    }
    return render(request , "index.html" , context)

def Add_dojo(request):
    models.create_dojo(request)
    return redirect('/')

def add_ninja(request):
    models.create_ninja(request)
    return redirect('/')