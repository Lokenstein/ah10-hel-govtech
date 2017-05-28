from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import UserProfile


class SignUpForm(UserCreationForm):
    location = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'location', 'password1', 'password2')