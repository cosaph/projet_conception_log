
# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

'''
L'idée ici c'est qu'on va créer une database (on bosse avec sql lite)
pour notre futur site.
On a besoin d'une  table user (username, mdp (chiffré), email, date d'inscription)
On aura besoin d'une table pour qu'un user ait une liste d'envie de ses courses à pieds préférées

'''

class User(AbstractUser):
    username = models.CharField(max_length=50,  null=True, blank=True)
    password = models.CharField(max_length=50,  null=True, blank=True)
    email = models.EmailField()
    date_inscription = models.DateTimeField('date d\'inscription', null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='user_set_polls',
        related_query_name='user_poll'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='user_set_polls',
        related_query_name='user_poll'
    )

    def save(self, *args, **kwargs):
        # Hasher le mot de passe avant d'enregistrer l'utilisateur
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
        
    def __object__(self):
        return self
    
    def was_inscrit_recently(self):
        return self.date_inscription >= timezone.now() - datetime.timedelta(days=1)



class Course(models.Model):
    nom_course= models.CharField(max_length=50)
    date_course = models.DateTimeField('date de la course')
    lieu_course = models.CharField(max_length=50)
    longueur = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_course
    
        
