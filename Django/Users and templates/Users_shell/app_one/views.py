from django.shortcuts import render, redirect
from .models import users


def index(request):
    context = {
        "all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)


def add_user(request):
    first_name = request.POST['first_username']
    last_name = request.POST['last_username']
    age = request.POST['user_age']
    email = request.POST['user_email']
    new_user = users.objects.create(first_name=first_name,
                                    last_name=last_name, age=age,
                                    email_address=email)
    return redirect('/')
