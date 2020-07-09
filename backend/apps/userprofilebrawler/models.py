from django.db import models
from apps.brawler.models import Brawler

# Create your models here.

class UserProfileBrawler(models.Model):
    brawler = models.ForeignKey(Brawler)
    level = models.IntegerField()
    power_points = models.IntegerField()
    equipments = models.ManyToManyField()
    abilities = models.ManyToManyField()


    def __str__(self):
        return f"Profil du: {self.brawler.name}"