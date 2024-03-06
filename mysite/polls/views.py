
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

def index(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


#https://www.runtrail.fr/events/search?date=2024-03-11%3B2024-03-17&region=bretagne&distance=0%3B15
def scrap(request):
    ville = request.GET.get('ville'),
    min_distance = request.GET.get('minDistance')
    max_distance = request.GET.get('maxDistance')

    base_url = "https://www.runtrail.fr/events/search"
    results = []
    results2 = []

    for page in range(1, 6):  # Loop through 5 pages
        query_params = {'region': ville, 'country': 'FR', 'page': page, 'distance': f'{min_distance};{max_distance}'}
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

    # Return the table HTML as the response
    return JsonResponse(response.url, safe=False)
    #return JsonResponse(table_html, safe=False)
