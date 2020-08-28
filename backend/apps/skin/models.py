from django.db import models


class Skin(models.Model):
    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(max_length=255)
    avatar = models.URLField()
    price = models.IntegerField()
    model_file = models.URLField()
    texture_file = models.URLField()
    voiceline_file = models.URLField()

    def __str__(self):
        return self.name
