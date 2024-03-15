# ------- Importing Libraries ------- #

"""
Le fichier apps.py est utilisé pour configurer l'application Django 'polls'.
Il permet de définir des options et des comportements spécifiques à cette application.
Dans notre cas, nous utilisons la classe 'PollsConfig' pour définir le champ auto-incrémenté 
par défaut pour les modèles de l'application 'polls' et spécifier le nom de l'application.
Ces configurations seront prises en compte lorsque nous utiliserons des fonctionnalités 
liées à l'application 'polls' dans notre projet Django.
"""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    Configuration de l'application 'polls' pour le projet Django.

    Cette classe permet de définir des configurations spécifiques à l'application 'polls',
    telles que le nom de l'application et le champ auto-incrémenté par défaut pour les modèles.

    Attributes:
        default_auto_field (str): Définit le type de champ auto-incrémenté par défaut pour  
                                les modèles.
                                Utilisé lorsque Django crée de nouveaux modèles ou ajoute des champs
                                auto-incrémentés à un modèle existant.
        name (str): Le nom complet du chemin de l'application, utilisé par Django pour identifier
                    l'application dans divers contextes, comme lors de l'utilisation 
                    des commandes `manage.py`.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
