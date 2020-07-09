from django.db import models
from apps.brawler.models import Brawler
from apps.projectilPattern.models import ProjectilPattern

# Create your models here.
class Ability(models.Model):
    brawler = models.ForeignKey(Brawler, on_delete=models.PROTECT)
    isSuper = models.BooleanField(default=False)
    name = models.CharField(max_length=125)
    description = models.TextField(default=' ')
    image = models.URLField(default=' ')
    reloadSpeed = models.DecimalField(decimal_places=2,max_digits=5,default =1)
    attackSpeed = models.DecimalField(decimal_places=2,max_digits=5,default =1)
    projectilPattern = models.ForeignKey(ProjectilPattern, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name