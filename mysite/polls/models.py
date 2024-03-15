"""
Fichier models.py - Définition des modèles de l'application.

Ce fichier contient la définition des modèles utilisés dans l'application,
qui sont des classes héritant de `django.db.models.Model`.
Les modèles définissent la structure et le comportement des données stockées
dans la base de données.

Pour plus d'informations sur la définition des modèles Django,
consultez la documentation officielle : https://docs.djangoproject.com/en/3.2/topics/db/models/
"""

from django.db import models
from django.contrib.auth.models import User


class ListItem(models.Model):
    """
    Modèle pour stocker les courses favorites d'un utilisateur.

    Attributs:
        user (ForeignKey): Référence à l'utilisateur Django auth.User 
                           qui possède cet élément de liste.
        content (CharField): Le contenu de l'élément de liste, 
                             par exemple, le nom de la course.
        created_at (DateTimeField): Date et heure de la création, 
                                    définies automatiquement.

    La logique de gestion des requêtes HTTP (méthodes `get` et `post`)
    est normalement gérée dans les vues plutôt que dans le modèle.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    form_class = None
    template_name = "list.html"