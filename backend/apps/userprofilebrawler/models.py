from django.db import models
from apps.brawler.models import Brawler
from apps.equipments.models import Equipment
from apps.abilities.models import Abilitie


# Create your models here.
class UserProfileBrawler(models.Model):
    brawler = models.ForeignKey(Brawler, on_delete=models.CASCADE)
    level = models.IntegerField()
    power_points = models.IntegerField()
    equipments = models.ManyToManyField(Equipment)
    abilities = models.ManyToManyField(Abilitie)


    def __str__(self):
        return f"Profil du: {self.brawler.name}"