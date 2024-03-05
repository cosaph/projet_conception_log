
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

from django.shortcuts import render

import json
from django.http import JsonResponse
from django.shortcuts import render


def scrap(request):
    ville = request.GET.get('ville')

    base_url = "https://www.runtrail.fr/events/search"
    query_params = {'region': ville}
    response = requests.get(base_url, params=query_params)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_elements = soup.find_all('a', class_="text-dark")
    results = [a.text for a in a_elements]

    # Return the results as JSON response
    return JsonResponse(response.url, safe=False)
