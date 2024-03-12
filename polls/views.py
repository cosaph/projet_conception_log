# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/08 09:14:40 by ccottet           #+#    #+#              #
#    Updated: 2024/03/10 21:38:11 by ccottet          ###   ########.fr        #
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


#### ----- Views ----- ####

def index(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def scrap(request):
    ville = request.GET.get('ville')
    min_distance = request.GET.get('minDistance')
    max_distance = request.GET.get('maxDistance')

    base_url = "https://www.runtrail.fr/events/search"
    results = []
    results2 = []

    for page in range(1, 6):
        query_params = {'region': ville, 'distance': f'{min_distance};{max_distance}', 'country': 'FR', 'page': page}
        response = requests.get(base_url, params=query_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        a_elements = soup.find_all('a', class_="text-dark")
        i_elements = soup.find_all('span', class_="city pt-2")

        results += [a.text for a in a_elements]
        results2 += [i.text for i in i_elements]

    # Generate HTML table
    table_html = '<table>'
    table_html += '<tr><th>Title</th><th>Lieu</th></tr>'
    for result, result2 in zip(results, results2):
        table_html += f'<tr><td>{result}</td><td>{result2}</td></tr>'
    table_html += '</table>'

    return table_html

def result(request):
    template = loader.get_template("polls/result.html")
    table_html = scrap(request)
    context = {'table_html': table_html}
    return HttpResponse(template.render(context, request))

# -- fonction test scrap image -- #

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

print(liste_elements)


from django.contrib.auth.models import User

def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('index')
    else:
        template = loader.get_template("polls/inscription.html")
        context = {}
        return HttpResponse(template.render(context, request))