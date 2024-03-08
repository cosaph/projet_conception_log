# Dans un fichier forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo', 'password', 'email']
