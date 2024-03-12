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
from django.contrib.auth import views as auth_views
from .views import list_view, delete_item_view, add_item

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # include result.html
    path('result.html', views.result, name='result'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('list/', list_view, name='list'),
    path('add_item/', add_item, name='add_item'),
    path('list/delete/<int:item_id>/', delete_item_view, name='delete_item'),
    # path pour récupérer les infos utiles au scraping
    path('submit-form', views.submit_form, name='submit_form'),
]