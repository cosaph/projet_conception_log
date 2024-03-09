# Dans un fichier forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(label='Nom d\'utilisateur ou adresse e-mail')
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
