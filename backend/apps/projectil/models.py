from django.db import models

class Projectil(models.Model):
    name = models.CharField(max_length=125)
    sprite = models.ImageField()
    speed = models.DecimalField()
    hitboxSize = models.DecimalField()
    damage = models.IntegerField()
    range = models.DecimalField()

    def __str__(self):
        return self.name
