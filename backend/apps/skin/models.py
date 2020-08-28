from django.db import models

# Create your models here.
class Skin(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    avatar = models.URLField()
    price = models.DecimalField(decimal_places=2,max_digits=5)
    ThreeDModelFile = models.URLField()
    TextureFile = models.URLField()
    VoiceLineFile = models.URLField()
    
    def __str__(self):
        return self.name