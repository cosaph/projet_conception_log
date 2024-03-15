# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/14 15:43:56 by ccottet           #+#    #+#              #
#    Updated: 2024/03/14 12:03:55 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Ce module définit les URL pour l'application de scraping de courses et trails.

Il associe les chemins d'URL aux vues spécifiques qui doivent être appelées lorsque 
ces URL sont sollicitées par un navigateur ou une requête HTTP. Cela permet de naviguer 
dans l'application web et d'accéder à ses différentes fonctionnalités.

Les routes disponibles sont :
- La page d'accueil, qui affiche le formulaire de recherche.
- La page de résultat, qui montre les résultats du scraping basé sur les 
critères de recherche soumis.
- Une action pour soumettre le formulaire de recherche, traitant les données 
du formulaire et retournant les résultats du scraping.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from polls import views
from .views import list_view, delete_item_view, add_item


urlpatterns = [
    # Page d'accueil : Affiche de le formulaire de recherche
    path("", views.index, name="index"),
    # Connexion
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # Déconnexion
    path("logout/", views.logout_view, name="logout"),
    # Inscription
    path("signup/", views.signup_view, name="signup"),
    # Liste de favoris
    path("list/", list_view, name="list"),
    # Ajout d'une course aux favoris
    path("add_item/", add_item, name="add_item"),
    # Suppression d'une course présente dans les favoris
    path("list/delete/<int:item_id>/", delete_item_view, name="delete_item"),
    # Suppression d'un compte
    path("delete-account/", views.delete_account, name="delete_account"),
    # Path pour récupérer les infos utiles au scraping
    path("submit-form", views.submit_form, name="submit_form"),
    #
    path("add_item/", views.add_item, name="add_item"),
    path("add_item/<int:fav_id>/", views.add_item, name="add_item"),
]
