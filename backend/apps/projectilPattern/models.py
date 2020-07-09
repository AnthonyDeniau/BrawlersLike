from django.db import models

# Create your models here.
class ProjectilPattern(models.Model):
    number = models.IntegerField()
    interval = models.DurationField()
    spreadAngle = models.DecimalField(decimal_places=10,max_digits=12)
    range = models.DecimalField(decimal_places=10,max_digits=12)

    def __str__(self):
        return self.number
