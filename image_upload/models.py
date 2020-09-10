from django.db import models

# Create your models here.
class Voter(models.Model):
    name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # first_time = 
    image = models.ImageField(upload_to='images/')