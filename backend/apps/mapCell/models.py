from django.db import models
from apps.map.models import Map
from apps.cellType.models import CellType

# Create your models here.


class MapCell(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    cell_type = models.ForeignKey(CellType, on_delete=models.CASCADE)
    position_x = models.IntegerField()
    position_y = models.IntegerField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.description

    def __str__(self):
        return self.position_x

    def __str__(self):
        return self.position_y
