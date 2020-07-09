from django.db import models

# Create your models here.
class Agility(models.Model):
    brawler = models.ForeignKey(),
    isSuper = models.BooleanField(),
    name = models.CharField(max_length=125),
    description = models.TextField(),
    image = models.URLField(), #ImageField ? requiert Pillow
    reloadSpeed = models.DecimalField(),
    attackSpeed = models.DecimalField(),
    projectilPattern = models.ForeignKey()
    def __str__(self):
        return self.name