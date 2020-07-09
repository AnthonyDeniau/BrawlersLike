from django.db import models

class Projectil(models.Model):
    name = models.CharField(max_length=125)
    sprite = models.URLField()
    speed = models.DecimalField(decimal_places=2, max_digits=5)
    hitboxSize = models.DecimalField(decimal_places=2, max_digits=5)
    damage = models.IntegerField()
    range = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name
