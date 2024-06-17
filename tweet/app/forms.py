from django import forms 
from .models import Tweet 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creating Tweet forms here.
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo'] 
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') # using tuple because using built in Custom User
        