from django.db import models
from .models import Brawler
from .models import ProjectilPattern

# Create your models here.
class Ability(models.Model):
    brawler = models.ForeignKey(Brawler, on_delete=models.PROTECT),
    isSuper = models.BooleanField(),
    name = models.CharField(max_length=125),
    description = models.TextField(),
    image = models.URLField(),
    reloadSpeed = models.DecimalField(),
    attackSpeed = models.DecimalField(),
    projectilPattern = models.ForeignKey(ProjectilPattern, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name