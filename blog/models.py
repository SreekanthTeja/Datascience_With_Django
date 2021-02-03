from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Journey(models.Model):
    journey_mode=models.CharField(max_length=250)
    def __str__(self):
        return self.journey_mode

class DreamTrip(models.Model):
    visitor=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Visitor")
    city_name=models.CharField(max_length=100,verbose_name="City")
    journey_type=models.ForeignKey(Journey,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Journey Mode')
    story=models.CharField(max_length=100,verbose_name="Story")
    budget=models.IntegerField(verbose_name="Budget")
    pictures=models.ImageField(upload_to='gallery',verbose_name="Pictures")

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse("details", args=[str(self.id)])
    