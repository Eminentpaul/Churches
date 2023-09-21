from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm




class AccountCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

