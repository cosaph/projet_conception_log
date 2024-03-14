"""
Ce fichier contient les tests unitaires pour les vues de l'application.

Il couvre les fonctionnalités principales des vues, telles que l'affichage de la page d'accueil,
le scraping de données et l'inscription d'un nouvel utilisateur.

Pour exécuter l'intégralité des tests :
- Utilisez la commande `python manage.py test` depuis la racine du projet (mysite).

Pour exécuter un test en particulier :
- Utilisez la commande `python manage.py test polls.tests.<NomDeLaClasseDeTest>.<nom_de_la_fonction_de_test>`.

Par exemple, pour exécuter le test `test_signup_view` de la classe `SignupViewTestCase` :
- Utilisez la commande `python manage.py test polls.tests.SignupViewTestCase.test_signup_view`.
"""

from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import scrap, signup_view


class IndexViewTest(TestCase):
    """
    Classe de test pour la vue d'accueil.
    """

    def test_index_view(self):
        """
        Vérifie si la vue d'accueil est accessible et utilise le bon template.

        Args:
            Aucune.

        Returns:
            - response: Objet HttpResponse de la requête HTTP.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/index.html")


class ScrapTestCase(TestCase):
    """
    Classe de test pour la fonction de scraping.
    """

    def setUp(self):
        """
        Configuration initiale des tests.

        """
        self.factory = RequestFactory()

    def test_scrap(self):
        """
        Vérifie si la fonction de scraping renvoie les données attendues.

        Args:
            - request: Objet HttpRequest de Django contenant les critères de recherche comme la ville,
                       la distance minimale et maximale.

        Returns:
            - response: Liste de dictionnaires avec les données scrapées ('title', 'city', 'img_url').
        """
        request = self.factory.post(
            "/scrap/", {"ville": "bretagne",
                        "minDistance": "10", "maxDistance": "20"}
        )
        response = scrap(request)

        self.assertIsInstance(response, list)

        expected_keys = ["title", "city", "img_url"]
        for data in response:
            self.assertCountEqual(expected_keys, data.keys())


class SignupViewTestCase(TestCase):
    """
    Classe de test pour la vue d'inscription.
    """

    def setUp(self):
        """
        Configuration initiale des tests.
        """
        self.factory = RequestFactory()

    def test_signup_view(self):
        """
        Vérifie si la vue d'inscription fonctionne correctement.

        Args:
            - request: Objet HttpRequest de Django contenant les paramètres de création de compte (username, password1, password2).

        Returns:
            - response: Objet HttpResponse de la redirection après l'inscription.
        """
        request = self.factory.post(
            "/signup/",
            {
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        response = signup_view(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/polls/login/")
