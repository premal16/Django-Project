from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser,UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.db import IntegrityError
from django.http import JsonResponse

def homePage(request):
    return render(request,'index.html')


def register_and_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        
        # Create the user
        user = CustomUser.objects.create_user(username=username, password=password, name=name, email=email)

        # Log in the user
        # user = authenticate(request, username=username, password=password)
        if user is not None:
            # auth_login(request, user)
            return redirect('login')
        else:
            return render(request, 'register.html', {'error_message': 'Error logging in after registration'})

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')
   


def profilePage(request):
    return render(request,'profile.html')


def logout_view(request):
    logout(request)
    return redirect('login') 




def edit_profile(request):
    user = request.user
    print(user.email)
    profile, created = UserProfile.objects.get_or_create(user=user)
    error_message = None 
    if request.method == 'POST':
        try:
            about = request.POST.get('about', '')
            profile_pic = request.FILES.get('profile_pic', None)
            job_title = request.POST.get('job_title', '')
            country = request.POST.get('country', '')
            address = request.POST.get('address', '')
            email = request.POST.get('email', '')
            mobile_number = request.POST.get('mobile_number')
            profile.job_title = job_title
            # Update profile fields and save
            profile.about = about
            profile.country = country
            profile.address = address
            profile.mobile_number = mobile_number
            user.email = email
            user.save()
            if profile_pic:
                profile.profile_pic = profile_pic
            profile.save()
            return redirect('profile')  
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e) and 'email' in str(e):
                error_message = "The provided email is already in use."
            else:
                error_message = "An error occurred while updating the profile." 
            
    return render(request, 'profile.html', {'error_message': error_message})