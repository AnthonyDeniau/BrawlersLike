from django.db import models

# Create your models here


class Map(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.description
