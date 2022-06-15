# from django.shortcuts import render

# # Create your views here.


from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Profile,Post, Rating
from .forms import PostForm, RatingsForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializar,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets



# Create your views here.

def welcome(request):
    # all_post=Post.objects.all()
    # all_post=random.sample(all_post,3)
    # a_post=Post.objects.all()
    # random_post=random.sample(a_post,3)
    
    # return render(request,'index.html',{"all_post":all_post,"random_post":random_post})
    
    
    all_post=Post.objects.all()
    all_post=all_post[::-1]
    a_post = random.randint(0, len(all_post)-1)
    random_post = all_post[a_post]

    return render(request,'index.html',{"all_post":all_post,"random_post":random_post})

def index(request):
    indexpost=Post.objects.filter(id=1)

    return render(request,'index.html',{"all_post":indexpost})    

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'login.html')
