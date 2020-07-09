from django.db import models
from apps.brawler.models import Brawler
from apps.equipment.models import Equipment
from apps.ability.models import Ability


# Create your models here.

class UserProfileBrawler(models.Model):
    brawler = models.ForeignKey(Brawler, on_delete=models.CASCADE)
    level = models.IntegerField()
    power_points = models.IntegerField()
    equipments = models.ManyToManyField(Equipment)
    abilities = models.ManyToManyField(Ability)


    def __str__(self):
        return f"Profil du: {self.brawler.name}"