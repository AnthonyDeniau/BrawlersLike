from django.db import models
from apps.brawler.models import Brawler


# Create your models here.
class UserProfile(models.Model):
    selected_brawler = models.ForeignKey(Brawler, on_delete=models.CASCADE)
    coins = models.IntegerField()
    trophy = models.IntegerField()
    gems = models.IntegerField()
    xp = models.IntegerField()
    
    def __str__(self):
        return f"Le profil de {self.selected_brawler.name}"
        