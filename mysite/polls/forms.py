from django import forms
from .models import ListItem

class ListItemForm(forms.ModelForm):
    """
    Formulaire Django pour la création et la mise à jour d'éléments ListItem.

    Ce formulaire est lié au modèle ListItem et permet à l'utilisateur de soumettre les données
    pour le champ 'content'. Cela facilite la création ou la mise à jour d'instances ListItem
    via des interfaces utilisateur web, en assurant la validation des données du formulaire
    et en appliquant automatiquement ces données au modèle associé.

    Attributs de Meta:
        model (Model): Le modèle Django auquel le formulaire est associé.
        fields (list): La liste des champs du modèle qui doivent être inclus dans le formulaire.
    """
    class Meta:
        model = ListItem
        fields = ['content']


