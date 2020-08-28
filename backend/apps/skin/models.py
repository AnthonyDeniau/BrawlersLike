from django.db import models

# Create your models here.
class Skin(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    avatar = models.URLField(default=' ')
    price = models.IntegerField()
    modelfile = models.URLField(default=' ')
    texturefile = models.URLField(default=' ')
    voicelinefile = models.URLField(default=' ')
    
def __str__(self):
        return self.name
    

    
