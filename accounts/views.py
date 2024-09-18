from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
def userRegister(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already Exist")
            else:
                user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                                password=password)
                user.save()
                profiles = Profile.objects.create(user=user, first_name=first_name, last_name=last_name,
                                                  mobile_no=mobile_no)
                profiles.save()
                messages.success(request, "User Registration Successful")
                return redirect('login')
        else:
            messages.error(request, "Password do not match")
    context = {
        'messages': messages,
    }
    return render(request, 'accounts/user_register.html', context)


def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Username & Password wrong ")
    return render(request, 'accounts/user_login.html')


def userLogout(request):
    logout(request)
    return redirect('login')
