from django.db import models

# Create your models here.
class Ability(models.Model):
    brawler = models.ForeignKey('brawler.Brawler', on_delete=models.PROTECT)
    isSuper = models.BooleanField()
    name = models.CharField(max_length=125)
    description = models.TextField()
    image = models.URLField()
    reloadSpeed = models.DecimalField(decimal_places=2,max_digits=5)
    attackSpeed = models.DecimalField(decimal_places=2,max_digits=5)
    projectilPattern = models.ForeignKey('projectilPattern.ProjectilPattern', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name