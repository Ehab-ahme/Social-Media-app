from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Profile
from .forms import SignUpForm, ProfileForm

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def settings(request):
    user_profile= Profile.objects.get(user=request.user)
    if request.method== 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form= ProfileForm(instance=user_profile)
    return render(request, 'setting.html', {"form": form, "user_profile": user_profile})


def signup(request):
    #Form Validation
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            #Crate new user
            user= form.save()
            
            #Create new Profile
            new_profile= Profile.objects.create(user= user, id_user= user.id)
            new_profile.save()
            auth.login(request, user=user)
            return redirect('settings')
        else:
            context= {"form": form}
            return render(request, 'signup.html', context)
        
    return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        user= auth.authenticate(username= username, password= password)
        # if user:
        if user is not None:
            auth.login(request, user= user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')