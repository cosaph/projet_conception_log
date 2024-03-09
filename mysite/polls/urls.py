# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/14 15:43:56 by ccottet           #+#    #+#              #
#    Updated: 2024/03/08 10:06:22 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # include result.html
    path('result', views.result, name='result'),
    
    path('register', views.register, name='register'),
]