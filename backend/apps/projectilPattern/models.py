from django.db import models

# Create your models here.
class Brawler(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    avatar = models.URLField()
    health = models.IntegerField()

    def __str__(self):
        return self.name
