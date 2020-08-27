from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    username = forms.CharField()
    class Meta:
        model = User
        fields = ('First_Name','Last_Name','Email','username','password1','password2')