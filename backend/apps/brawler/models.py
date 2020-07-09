from django.db import models
from django_enumfield import enum


class Rarity(enum.Enum):
    CLASSIC = 0
    RARE = 1
    SUPER_RARE = 2
    EPIC = 3
    MYTHIC = 4
    LEGENDARY = 5
    CHROMATIC = 6


class Brawler(models.Model):
    name = models.CharField(max_length=125)
    cost = models.IntegerField()
    description = models.TextField(max_length=255)
    avatar = models.URLField()
    rarity = enum.EnumField(Rarity)
    health = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name
