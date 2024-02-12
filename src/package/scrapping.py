# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scrapping.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/12 14:40:58 by ccottet           #+#    #+#              #
#    Updated: 2024/02/12 15:20:58 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


## ---- Module ---- ##

import requests
from bs4 import BeautifulSoup

## ---- Scrapping de Klikego ---- ##

url = "https://klikego.com/recherche"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

a_elements = soup.find_all('a', class_ = 'texte-vert-fonce')
span_location = soup.find_all('span', class_ = 'texte-localisation')


output =[]
output2 = []

for item in a_elements:
        output.append(item.text.strip())

for item in span_location:
    item = item.text.strip()
    item = item.replace('\t', '')
    item = item.replace('\n', '')
    item = item.replace('\r', '')
    item = item.replace(' ', '')
    output2.append(item)
    
print(output)
print(output2)