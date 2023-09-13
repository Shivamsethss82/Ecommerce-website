from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf.urls.static import static


# Create your views here.

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'authentication/signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                messages.info(request,"Email is Taken")
                return render(request,'authentication/signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
    return render(request, 'authentication/signup.html')


def handlelogin(request):
    return render(request, 'authentication/login.html')


def handlelogout(request):
    return redirect('/auth/login')