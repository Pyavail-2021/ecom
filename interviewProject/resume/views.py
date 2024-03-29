from urllib import request
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render,redirect
from . models import Category , Post

# Create your views here.

def index(request):
    category=Category.objects.all()
    return render(request , 'index.html',{'category':category})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email):
                messages.info(request,'email exists already')
                return redirect('signup')
            elif User.objects.filter(username=username):
                messages.info(request ,'username exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username , email=email, password=password2)
                user.save();
                return redirect('login')
        else:
            messages.info(request , 'password is not same')
            return redirect('signup')
    else:
        return render(request , 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request , user)
            return redirect('/')
    else:
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/blog')

def blog(request):
    post= Post.objects.all()

    return render(request , 'blog.html' , {'post':post})

def blog_single(request):
    post= Post.objects.all()
    return render(request , 'blog-single.html', {'post':post})

def shop(request):

    return render(request , 'shop.html')



def contact(request):
    return render(request , 'contact.html')