from .models import profile
from django import forms
from django.contrib.auth.models import User


class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']