from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from django.template import loader
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import ListItem
from .forms import ListItemForm

# Create your tests here.
from .views import index

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('nom_de_votre_vue_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/index.html')

from .views import scrap

class ScrapViewTest(TestCase):
    def test_scrap_view(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['ville'] = 'nom_de_la_ville'
        request.POST['minDistance'] = 'valeur_min_distance'
        request.POST['maxDistance'] = 'valeur_max_distance'

        response = scrap(request)

        self.assertEqual(response.status_code, 200)  
        self.assertIsInstance(response, list)  

from .views import result

class ResultViewTest(TestCase):
    def test_result_view(self):
        request = HttpRequest()
        request.method = 'GET'

        response = result(request)

        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'polls/result.html')  

        self.assertIn('table_html', response.context)

from .views import submit_form

class SubmitFormViewTest(TestCase):
    def test_submit_form_view_post(self):
        request = HttpRequest()
        request.method = 'POST'

        response = submit_form(request)

        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'polls/scrap_result.html')  
    def test_submit_form_view_get(self):
        request = HttpRequest()
        request.method = 'GET'

        response = submit_form(request)

        self.assertEqual(response.status_code, 405)  

from .views import signup_view

class SignUpViewTest(TestCase):
    def test_signup_view_post(self):
        request = HttpRequest()
        request.method = 'POST'

        response = signup_view(request)

        self.assertTrue(User.objects.exists())

        self.assertRedirects(response, reverse('login'))

    def test_signup_view_get(self):
        request = HttpRequest()
        request.method = 'GET'

        response = signup_view(request)

        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'signup.html') 

from .views import delete_account

class DeleteAccountViewTest(TestCase):
    def test_delete_account_view_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='password123')  # Crée un utilisateur de test
        login(request, request.user)  # Connecte l'utilisateur simulé

        response = delete_account(request)

        self.assertFalse(User.objects.filter(username='testuser').exists())

        self.assertFalse(request.user.is_authenticated)

        self.assertRedirects(response, reverse('index'))

    def test_delete_account_view_get(self):
        request = HttpRequest()
        request.method = 'GET'

        response = delete_account(request)

        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'delete_account.html')  

from .views import logout_view

class LogoutViewTest(TestCase):
    def test_logout_view(self):
        request = HttpRequest()
        request.method = 'GET'
        user = User.objects.create_user(username='testuser', password='password123')  
        request.user = user
        login(request, user)  
        response = logout_view(request)

        self.assertFalse(request.user.is_authenticated)

        self.assertRedirects(response, reverse('index'))

from .views import list_view
class ListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_list_view_get(self):
        request = HttpRequest()
        request.method = 'GET'
        request.user = self.user

        response = list_view(request)

        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'list.html')  

    def test_list_view_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['item_name'] = 'Test Item'

        response = list_view(request)

        self.assertTrue(ListItem.objects.filter(user=self.user, item_name='Test Item').exists())

        self.assertRedirects(response, reverse('list'))

from .views import add_item

class AddItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_add_item_view_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['title'] = 'Test Title'
        request.POST['city'] = 'Test City'

        response = add_item(request)

        self.assertTrue(ListItem.objects.filter(user=self.user, content='Test Title, Test City').exists())

        self.assertTemplateUsed(response, 'list.html')

        self.assertEqual(response.context['title'], 'Test Title')
        self.assertEqual(response.context['city'], 'Test City')

    def test_add_item_view_get(self):
        request = HttpRequest()
        request.method = 'GET'

        response = add_item(request)

        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.content.decode('utf-8'), 'Invalid request')  


from .views import delete_item_view

class DeleteItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_delete_item_view(self):
        item = ListItem.objects.create(user=self.user, content="Test item content")

        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user

        response = delete_item_view(request, item.id)

        self.assertFalse(ListItem.objects.filter(id=item.id).exists())

        self.assertRedirects(response, reverse('list'))

