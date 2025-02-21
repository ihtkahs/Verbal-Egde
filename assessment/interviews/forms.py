from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)  # Optional phone number

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
