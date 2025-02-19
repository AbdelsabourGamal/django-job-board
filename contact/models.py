from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Info(models.Model):
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.email




