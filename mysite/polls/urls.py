# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ccottet <ccottet@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/14 15:43:56 by ccottet           #+#    #+#              #
#    Updated: 2024/03/04 14:27:41 by ccottet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/

]