from django.db import models

# Create your models here.
class ProjectilPattern(models.Model):
    number = models.IntegerField()
    interval = models.DurationField()
    spreadAngle = models.DecimalField()
    range = models.DecimalField()

    def __str__(self):
        return self.number
