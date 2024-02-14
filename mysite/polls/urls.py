# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/14 15:43:56 by ccottet           #+#    #+#              #
#    Updated: 2024/02/14 15:43:57 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]