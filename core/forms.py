from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    def clean_email(self):
        email= self.cleaned_data['email']
        if User.objects.filter(email= email).exists():
            raise forms.ValidationError("Email Taken")
        return email

    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.filter(username= username).exists():
            raise forms.ValidationError("Username Taken")
        return username

    class Meta:
        model= User
        fields= ["username", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['bio', 'location', 'profile_img']