from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=125)
    cost = models.IntegerField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name
