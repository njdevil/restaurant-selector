# Restaurant Selector v0.1
# https://github.com/njdevil/restaurant-selector
# &copy;2013 Modular Programming Systems Inc
# released as GPL 3

from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

