from django.shortcuts import render , redirect
from .models import users

def index(request):
    context = {
        "all_the_users": users.objects.all()  
    }
    return render (request , "index.html" , context)

def add_user(request):
    request.session['first_name'] = request.POST['first_username'] 
    request.session['last_name'] = request.POST['last_username'] 
    request.session['uesr_age'] = request.POST['user_age'] 
    request.session['user_email'] = request.POST['user_email']
    new_user = users.objects.create(first_name= request.session['first_name'] , 
        last_name = request.session['last_name'] , age = request.session['uesr_age'] , 
        email_address =  request.session['user_email'])
    return redirect('/')