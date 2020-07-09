from django.db import models

# Create your models here.
class Ability(models.Model):
    brawler = models.ForeignKey(models.Brawler, on_delete=models.PROTECT),
    isSuper = models.BooleanField(),
    name = models.CharField(max_length=125),
    description = models.TextField(),
    image = models.URLField(),
    reloadSpeed = models.DecimalField(),
    attackSpeed = models.DecimalField(),
    projectilPattern = models.ForeignKey(models.projectilPattern, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name