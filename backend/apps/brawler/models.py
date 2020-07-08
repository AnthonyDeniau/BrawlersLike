from django.db import models


class Brawler(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
