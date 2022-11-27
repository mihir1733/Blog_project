from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from.forms import SignUpForm,LoginForm,PostForm
from.models import BlogPost

from django.contrib import messages

def home(request):
    post = BlogPost.objects.all
    return render(request,'home.html',{'post':post})




def about(request):
    return render(request,'about.html')




def contact(request):
    return render(request,'contact.html')




def dashboard(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'dashboard.html',{'posts':posts,'full_name':full_name,'gps':gps})
    else:
        return HttpResponseRedirect('/login/')
    



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrates!! You have successfully created your account and now you are Author please go to login page!')
            user=form.save()
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
            
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def loginuser(request):
    if not request.user.is_authenticated:
        
     if request.method == 'POST':
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = uname , password = upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Welcome! Successfully Logged in')
                return HttpResponseRedirect('/dashboard/')
     else:
        form = LoginForm()
     return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')
    


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                pst = BlogPost(title=title,description=description)
                pst.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form= PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def updatepost(request,id=0):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pst = BlogPost.objects.get(id = id)
            form = PostForm(request.POST,instance=pst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pst = BlogPost.objects.get(id=id)
            form = PostForm(instance=pst)
        return render(request,'updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request,id=0):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(id=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')