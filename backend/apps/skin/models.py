from django.db import models


# Create your models here.
class Skin(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=255)
    avatar = models.URLField()
    price = models.IntegerField()
    modelFile = models.URLField()
    textureFile = models.URLField()
    voiceLineFile = models.URLField()


    def __str__(self):
        return self.name
        