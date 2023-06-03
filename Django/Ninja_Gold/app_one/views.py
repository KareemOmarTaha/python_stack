from django.shortcuts import render, redirect
import random


def index(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
    context = {
        "gold": request.session['your_gold']
    }
    return render(request, "index.html", context)


def get_farm(request):
    request.session['your_gold'] += random.randint(10, 20)
    return redirect("/")


def get_cave(request):
    request.session['your_gold'] += random.randint(10, 20)
    return redirect("/")


def get_house(request):
    request.session['your_gold'] += random.randint(10, 20)
    return redirect("/")


def get_quest(request):
    request.session['your_gold'] += random.randint(-50, 50)
    return redirect("/")

def reset_gold (request):
    del request.session['your_gold']
    return redirect("/")