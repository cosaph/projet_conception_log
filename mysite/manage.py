#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Ce script est l'outil de ligne de commande généré automatiquement par Django pour le projet.
Il permet d'exécuter diverses tâches administratives et de gestion, 
telles que le démarrage d'un serveur de développement,
la création de migrations, l'application de migrations, et l'exécution de tests.

Il agit comme une interface de ligne de commande pour les fonctionnalités offertes
par le framework Django,
facilitant ainsi le développement, la configuration et la gestion du projet.

Usage:
    python manage.py [command] [options]

Examples:
    python manage.py runserver
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py test

Pour une liste complète des commandes disponibles, utilisez:
    python manage.py help
"""

import os
import sys
from django.core.management import execute_from_command_line


def main():
    """
    Fonction principale exécutant les tâches administratives.

    Cette fonction configure l'environnement du projet en définissant le module 
    de paramètres Django par défaut et délègue ensuite l'exécution à Django via 
    `execute_from_command_line`.
    Elle attrape et relève également une exception si Django n'est pas correctement importé,
    ce qui peut indiquer un problème avec l'installation de Django ou 
    la configuration de l'environnement.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == "__main__":
    main()
