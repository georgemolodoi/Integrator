from django.db import models

# Create your models here.
class ArtworksDB(models.Model):
    image = models.ImageField(upload_to='UploadedImages', blank=False)