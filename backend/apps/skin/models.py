from django.db import models
from django.contrib.auth.models import User


class Name(models.Model):
    name = models.CharField(max_length=125)
    Description = models.TextField()
    Avatar = models.URLField()
    Price = models.IntegerField()
    ModelFile = models.URLField()
    TextureFile = models.URLField()
    VoiceLineFile = models.URLField()

    def __str__(self):
        return self.name
