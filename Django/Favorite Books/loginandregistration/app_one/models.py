from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        x = User.objects.filter(email=postData['email'])    
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password description should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Password conformation didn't match"
        if  len(x)>0:
            errors['emaill'] = "Email Already Used!"

        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['book_title']) < 1:
            errors["title"] = "Book Title is required"
        if len(postData['book_desc']) < 3:
            errors["desc"] = "Book Description is required"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books", on_delete = models.CASCADE)
    users_who_like= models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()

def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['fname'] ,last_name = request.POST['lname'] , email = request.POST['email'] , 
                        password= pw_hash )
    

def get_user(request):
    return User.objects.get(id=request.session['userid']) 


def create_a_book(request):
    book_title = request.POST['book_title']
    book_desc = request.POST['book_desc']
    book_user = User.objects.get(id=request.session['userid'])
    Book.objects.create(title=book_title ,description=book_desc,uploaded_by = book_user)
    book = Book.objects.last()
    book_user.liked_books.add(book)

def view_book_models():
    return Book.objects.all()

def add_to_fav(request , ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=ID)
    user.liked_books.add(book)

def remove_from_fav(request,ID):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=ID)
    user.liked_books.remove(book)

def show_details(num):
    return Book.objects.get(id=num)

def update_book(request , num):
    update_desc = Book.objects.get(id=num)
    update_desc.description = request.POST['book_desc']
    update_desc.save()


def delete_book(request , num):
    book_to_delete = Book.objects.get(id=num)
    book_to_delete.delete()