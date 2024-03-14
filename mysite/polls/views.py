# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/08 09:14:40 by ccottet           #+#    #+#              #
#    Updated: 2024/03/14 12:16:04 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#### ----- Libraries ----- ####
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from django.http import HttpResponse
import csv
import json
from django.urls import path
from django.template.loader import get_template
from django.template import loader
from django.http import JsonResponse
from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect
import urllib.parse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from .models import ListItem
from .forms import ListItemForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from .models import ListItem



#### ----- Views ----- ####

def index(request):
    """
    Affiche la page d'accueil de l'application.

    Args:
        request: Objet HttpRequest de Django.

    Returns:
        HttpResponse: Rendu du template de l'index.
    """
    template = loader.get_template("polls/index.html")

    context = {}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def scrap(request):
    """
    Effectue le scraping des données des événements de course basé sur les critères spécifiés dans la requête POST.

    Args:
        request: Objet HttpRequest de Django contenant les critères de recherche comme la ville, 
                 la distance minimale et maximale.

    Returns:
        List[Dict]: Liste de dictionnaires avec les données scrapées ('title', 'city', 'img_url').
    """
    if request.method == "POST":
        ville = request.POST.get('ville')
        min_distance = request.POST.get('minDistance')
        max_distance = request.POST.get('maxDistance')

        base_url = "https://www.runtrail.fr/events/search"
        scraped_data = []

        for page in range(1, 6):
            query_params = {'region': ville, 'distance': f'{min_distance};{max_distance}', 'country': 'FR', 'page': page}
            response = requests.get(base_url, params=query_params)
            soup = BeautifulSoup(response.text, 'html.parser')
            a_elements = soup.find_all('a', class_="text-dark")
            i_elements = soup.find_all('span', class_="city pt-2")
            img_tags = soup.find_all('img', class_="img-fluid")
            image_urls = [img.get('data-src') for img in img_tags if img.get('data-src')]

            for title, city, img_url in zip(a_elements, i_elements, image_urls):
                image_urls = "https://www.runtrail.fr/" + img_url
                scraped_data.append({'title': title.text, 'city': city.text, 'img_url': image_urls})

        return scraped_data  # Retourne les données au lieu de HTML



@csrf_exempt
def submit_form(request):
    """
    Gère la soumission du formulaire de recherche et affiche les résultats du scraping.

    Args:
        request: Objet HttpRequest de Django.

    Returns:
        HttpResponse: Rendu du template des résultats de scraping si la méthode est POST ; sinon, renvoie une erreur HTTP 405.
    """
    if request.method == 'POST':
        # Appel de la fonction de scraping avec les données du formulaire
        scraped_data = scrap(request)  # Assurez-vous que cette fonction attend et traite les données POST
        
        # Rendu du template avec les données de scraping
        return render(request, 'polls/scrap_result.html', {'scraped_data': scraped_data})
    else:
        return HttpResponse("Méthode non autorisée.", status=405)


def signup_view(request):
    """
    Gère le processus d'inscription des utilisateurs.

    Si la méthode est POST et que le formulaire est valide, enregistre un nouvel utilisateur
    et redirige vers la page de connexion. Sinon, affiche un formulaire d'inscription vide.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Le rendu du template 'signup.html' avec le formulaire d'inscription.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def delete_account(request):
    """
    Permet à l'utilisateur connecté de supprimer son compte.

    Après la suppression, l'utilisateur est déconnecté et redirigé vers la page d'accueil.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Redirection vers la page d'accueil après suppression du compte.
    """
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('index')
    return render(request, 'delete_account.html')

@require_POST
@login_required
def logout_view(request):
    """
    Déconnecte l'utilisateur et redirige vers la page d'accueil.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Redirection vers la page d'accueil.
    """
    logout(request)
    return redirect(reverse('index'))



@login_required
def list_view(request):
    """
    Affiche la liste des courses favorites de l'utilisateur connecté et gère l'ajout de nouvelles courses

    Si la méthode est POST et que le formulaire est valide, ajoute un nouvel élément à la liste
    de l'utilisateur et redirige vers la même vue. Sinon, affiche les éléments existants et un
    formulaire pour ajouter un nouvel élément.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Le rendu du template 'list.html' avec les éléments de la liste et le formulaire.
    """
    user = request.user
    items = ListItem.objects.filter(user=user)

    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return redirect('list')
    else:
        form = ListItemForm()

    context = {
        'items': items,
        'form': form
    }

    return render(request, 'list.html', context)



@login_required
def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        city = request.POST.get('city')

        # Create a new ListItem instance and save it to the database
        item = ListItem(user=request.user, content=f"{title}, {city}")
        item.save()
        
        # Pass the data as context variables to the template
        return render(request, 'list.html', {'title': title, 'city': city})
    
    return HttpResponse('Invalid request')


@login_required
def delete_item_view(request, item_id):
    """
    Supprime un élément spécifié par son id et redirige vers la vue de la liste.

    Args:
        request: L'objet HttpRequest.
        item_id: L'identifiant de l'élément à supprimer.

    Returns:
        HttpResponseRedirect vers la vue de la liste après la suppression de l'élément.
    """
    item = ListItem.objects.get(id=item_id)
    item.delete()
    return redirect('list')