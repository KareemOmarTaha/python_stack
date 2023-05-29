from django.shortcuts import render , redirect
import random
def index (request):
    request.session['rand_num'] = random.randint(1,100) 
    print(request.session['rand_num'])
    return render(request , "index.html")

def calc_rand(request):
    rand_form = request.POST['rand_input']
    print(int(rand_form))
    if int(rand_form) == request.session['rand_num']:
        return redirect('/equal')
    elif int(rand_form) > request.session['rand_num']:
        return redirect ('/high')
    elif int(rand_form) < request.session['rand_num']:
        return redirect ('/low')

def equal_res(request):
    return render(request , 'equal.html')

def higher(request):
    return render(request , 'high.html')

def lower(request):
    return render(request , 'low.html')

def play_again(request):
    return redirect('/')