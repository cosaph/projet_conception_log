
# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

'''
L'idée ici c'est qu'on va créer une database (on bosse avec sql lite)
pour notre futur site.
On a besoin d'une  table user (pseudo, mdp (chiffré), email, date d'inscription)
On aura besoin d'une table pour qu'un user est une liste d'envie de ses courses à pieds préférées

'''

class User(models.Model):
    pseudo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    date_inscription = models.DateTimeField('date d\'inscription')

    def __str__(self):
        return self.pseudo
    def was_inscrit_recently(self):
        return self.date_inscription >= timezone.now() - datetime.timedelta(days=1)
    


class Course(models.Model):
    nom_course= models.CharField(max_length=50)
    date_course = models.DateTimeField('date de la course')
    lieu_course = models.CharField(max_length=50)
    longueur = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_course
    
        
