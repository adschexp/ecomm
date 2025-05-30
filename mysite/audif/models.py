from django.db import models

# Create your models here.
  

class Producto(models.Model):
    Title = models.CharField(max_length=100)
    Price = models.FloatField()
    Imagen = models.ImageField(upload_to = 'images/', default='audif1.jpeg')