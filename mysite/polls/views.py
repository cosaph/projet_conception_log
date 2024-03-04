
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

def index(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def scrap(request):
    # je souhaite récuperer l'input "ville" ce index.html pour l'utiliser dans ma requête
    
    url = "https://www.runtrail.fr/events/search"
    ville = request.GET.get('ville')
    params = {'city=' : ville}
    response = requests.get(url, params=ville)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_element = soup.find_all('a', class_ = "text-dark")
    for a in a_element:
        print(a.text)

