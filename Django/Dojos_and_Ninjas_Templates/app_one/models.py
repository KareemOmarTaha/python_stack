from django.db import models 

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=10)
    desc=models.TextField(default="old Dojo")

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo,related_name="ninjas",on_delete = models.CASCADE)

def show_dojos ():
    dojo_name = Dojo.objects.all()
    return dojo_name

def show_ninja():
    ninja_name = Ninja.objects.all()
    return ninja_name

def create_dojo(request):
    new_dojo = Dojo.objects.create(name = request.POST['dojo_name'] , city = request.POST['dojo_city'], state = request.POST['dojo_state'])
    return new_dojo

def create_ninja(request):
    new_ninja = Ninja.objects.create(first_name = request.POST['ninja_first_name'] , last_name=request.POST['ninja_last_name'],dojo=Dojo.objects.get(id=request.POST['dojos']))
    return new_ninja


