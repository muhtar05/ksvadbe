from django.db import models
from sorl.thumbnail import ImageField



class Photo(models.Model):
    image = ImageField(upload_to='demo/photo')

