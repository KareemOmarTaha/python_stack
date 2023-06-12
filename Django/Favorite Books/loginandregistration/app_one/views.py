from django.shortcuts import render, redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import User , Book
import bcrypt

def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        models.register(request)
        
        return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['person_email'])
    if user :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id

            return redirect('/books')
    return redirect('/')

def view_book(request):
    context = {
            "welcome" : models.get_user(request), 
            "books" : models.view_book_models() , 
        }
    if request.session['userid']:
        return render(request,'welcome.html' , context)
    else:
        redirect('/')

def logout(request):
    del request.session['userid']
    return redirect('/')

def create_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        models.create_a_book(request)
        return redirect ('/books')

def add_favorite(request , ID):
    models.add_to_fav(request , ID)
    return redirect(request.META['HTTP_REFERER'])

def show_details(request , num):
    context = {
    "book_id":models.show_details(num),
    "user_id":models.get_user(request),
    }
    if models.User.objects.get(id=request.session['userid'])  == models.Book.objects.get(id = num).uploaded_by:
        return render (request , 'Uploader.html' ,context)
    else:
        return render (request , 'Viewer.html' ,context)
    

def remove_favorite(request , ID):
    models.remove_from_fav( request ,ID)
    return redirect('/books')

def updated_book(request , num):
    models.update_book(request , num)
    return redirect('/books')

def delete_book(request , num):
    models.delete_book(request , num)
    return redirect('/books')