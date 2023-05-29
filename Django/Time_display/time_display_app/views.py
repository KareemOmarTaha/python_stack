from django.shortcuts import render
from time import strftime

def check_time (request):
    context = {
        "time1" : strftime("%b %d, %Y"),
        "time2" : strftime("%H:%M %p")
    }
    return render(request, "index.html", context)
