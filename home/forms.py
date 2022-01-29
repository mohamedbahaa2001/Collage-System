
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=101)
    # last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    phone = forms.CharField(max_length=101)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'phone', 'email', 'password1', 'password2']