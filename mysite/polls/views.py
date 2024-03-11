# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/08 09:14:40 by ccottet           #+#    #+#              #
#    Updated: 2024/03/11 14:56:08 by ccottet          ###   ########.fr        #
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



#### ----- Views ----- ####

def index(request):
    template = loader.get_template("polls/index.html")

    context = {}
    return HttpResponse(template.render(context, request))


import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def scrap(request):

    if request.method == "POST":
        ville = request.POST.get('ville')
        min_distance = request.POST.get('minDistance')
        max_distance = request.POST.get('maxDistance')

        base_url = "https://www.runtrail.fr/events/search"
        results = []
        results2 = []
        results3 = []

        for page in range(1, 6):
            query_params = {'region': ville, 'distance': f'{min_distance};{max_distance}', 'country': 'FR', 'page': page}
            response = requests.get(base_url, params=query_params)
            soup = BeautifulSoup(response.text, 'html.parser')
            a_elements = soup.find_all('a', class_="text-dark")
            i_elements = soup.find_all('span', class_="city pt-2")
            img_tags = soup.find_all('img', class_="img-fluid")
            image_urls = []
            for img in img_tags:
                src = img.get('data-src')
                if src:
                    image_urls.append(src)
                    results3 = [base_url + element for element in image_urls]

            results += [a.text for a in a_elements]
            results2 += [i.text for i in i_elements]

        # Give me the URL with query parameters
        url = f"https://www.runtrail.fr/events/search?region={ville}&distance={min_distance};{max_distance}&country=FR&page=1"
        table_html = '<table>'
        table_html += '<tr><th>Title</th><th>Lieu</th><th>Image</th></tr>'
        for result, result2, result3 in zip(results, results2, results3):
            table_html += f'<tr><td>{result}</td><td>{result2}</td><td><img src="{result3}" alt="Image"></td></tr>'
            table_html += f'<tr><td><a href="{url}">Lien</a></td></tr>'
        table_html += '</table>'
        return HttpResponse(table_html)


def result(request):
    template = loader.get_template("polls/result.html")
    table_html = scrap(request)
    context = {'table_html': table_html}
    return HttpResponse(template.render(context, request))

""" # -- fonction test scrap image -- #

url = "https://www.runtrail.fr/events/search?region=bretagne&elevation=50;500&country=FR&page=2"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img', class_="img-fluid")

image_urls = []
for img in img_tags:
    src = img.get('data-src')
    if src:
        image_urls.append(src)

url_trail = "https://www.runtrail.fr/"

liste_elements = [url_trail + element for element in image_urls]

print(liste_elements) """

@require_POST
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def list_view(request):
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
    # Logique pour l'ajout d'un élément
    return redirect('list')  # Remplacez 'list' par le nom de la vue correspondant à votre liste d'éléments

@login_required
def delete_item_view(request, item_id):
    item = ListItem.objects.get(id=item_id)
    item.delete()
    return redirect('list')