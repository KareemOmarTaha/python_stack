from django.shortcuts import render , redirect

def show (request):
    return render (request , "index.html")

def showResult(request):
    name_form = request.POST["username"]
    location_form = request.POST["cities"]
    lang_form = request.POST["lang"]
    comment_form = request.POST["comments"]
    context = {
        "name_on_temp": name_form,
        'location_on_temp' : location_form,
        'lang_on_temp' : lang_form,
        'comment_on_temp' : comment_form
    }
    return render ( request , 'result.html' , context)

