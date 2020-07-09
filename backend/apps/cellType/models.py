from django.db import models

# Create your models here.


class CellType(models.Model):
    name = models.CharField(max_length=125)
    sprite = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.sprite
