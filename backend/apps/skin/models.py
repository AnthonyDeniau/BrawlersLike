from django.db import models
from django_enumfield import enum

# Définition du modèle

class Skin(models.Model):
    name = models.CharField(max_length=255, unique=True)
    Description = models.CharField(max_length=500)
    Avatar = models.URLField(max_length= 500)
    Price = models.IntegerField()
    Model3DFile = models.URLField(max_length= 500)
    TextureFile = models.URLField(max_length= 500)
    VoiceLineFile = models.URLField(max_length= 500)

# Retourne par defaut le nom du skin
def str(self):
    return self.name