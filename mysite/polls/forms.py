from django import forms
from .models import ListItem

class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['content']



class ConnexionForm(forms.Form):
    nom_utilisateur = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)