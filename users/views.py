from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import  User
from .models import Profile
from .forms import  CustomUserCreationForm



#logout - take user request and delete session id 

# Create your views here.
#(creating function base view)

def loginUser(request):
    page = 'login'
    #block user from entering login page after login
    if request.user.is_authenticated:
         return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        try:
            user =  User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
        # create session for user in database
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request, 'users/loging_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')

    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #hold user data before processing 
            user = form.save(commit= False)
            #to prevent same name in capital and simple 
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('profiles')
        
        else:
         messages.error(request, 'An error has occured during registration')


    context = {'page':page, 'form':form}
    return  render(request, 'users/loging_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, "otherSkills": otherSkills }
    return render(request, 'users/user-profile.html', context)


def autofill_redirect(request):
    return render(request, '/graphic/login_gp.html')


