# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/08 09:14:40 by ccottet           #+#    #+#              #
#    Updated: 2024/03/12 11:04:30 by ccottet          ###   ########.fr        #
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

from django.views.decorators.csrf import csrf_exempt



#### ----- Views ----- ####

def index(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

# def scrap(request):

#     if request.method == "POST":
#         ville = request.POST.get('ville')
#         min_distance = request.POST.get('minDistance')
#         max_distance = request.POST.get('maxDistance')

#         base_url = "https://www.runtrail.fr/events/search"
#         results = []
#         results2 = []
#         results3 = []

#         for page in range(1, 6):
#             query_params = {'region': ville, 'distance': f'{min_distance};{max_distance}', 'country': 'FR', 'page': page}
#             response = requests.get(base_url, params=query_params)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             a_elements = soup.find_all('a', class_="text-dark")
#             i_elements = soup.find_all('span', class_="city pt-2")
#             img_tags = soup.find_all('img', class_="img-fluid")
#             image_urls = []
#             for img in img_tags:
#                 src = img.get('data-src')
#                 if src:
#                     image_urls.append(src)
#                     results3 = [base_url + element for element in image_urls]

#             results += [a.text for a in a_elements]
#             results2 += [i.text for i in i_elements]

#         # Give me the URL with query parameters
#         url = f"https://www.runtrail.fr/events/search?region={ville}&distance={min_distance};{max_distance}&country=FR&page=1"
#         table_html = '<table>'
#         table_html += '<tr><th>Title</th><th>Lieu</th><th>Image</th></tr>'
#         for result, result2, result3 in zip(results, results2, results3):
#             table_html += f'<tr><td>{result}</td><td>{result2}</td><td><img src="{result3}" alt="Image"></td></tr>'
#             table_html += f'<tr><td><a href="{url}">Lien</a></td></tr>'
#         table_html += '</table>'
#         return HttpResponse(table_html)

@csrf_exempt
def scrap(request):
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


def result(request):
    template = loader.get_template("polls/result.html")
    table_html = scrap(request)
    context = {'table_html': table_html}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        # Appel de la fonction de scraping avec les données du formulaire
        scraped_data = scrap(request)  # Assurez-vous que cette fonction attend et traite les données POST
        
        # Rendu du template avec les données de scraping
        return render(request, 'polls/scrap_result.html', {'scraped_data': scraped_data})
    else:
        return HttpResponse("Méthode non autorisée.", status=405)

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