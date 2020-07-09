from django.db import models
from BrawlersLike.backend.apps.brawler import Brawler
from BrawlersLike.backend.apps.projectilPattern import ProjectilPattern

# Create your models here.
class Agility(models.Model):
    brawler = models.ForeignKey(Brawler, on_delete=models.PROTECT),
    isSuper = models.BooleanField(),
    name = models.CharField(max_length=125),
    description = models.TextField(),
    image = models.URLField(), #ImageField ? requiert Pillow
    reloadSpeed = models.DecimalField(),
    attackSpeed = models.DecimalField(),
    projectilPattern = models.ForeignKey(projectilPattern, on_delete=models.PROTECT)
    def __str__(self):
        return self.name