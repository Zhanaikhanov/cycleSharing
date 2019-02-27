from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Bicycle(models.Model):
	type_b = models.CharField(max_length=30)
	style = models.CharField(max_length=30)
	image = models.CharField(max_length=190)
	cost = models.IntegerField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	stars = models.IntegerField()

class BicycleRent(models.Model):
	renter = models.ForeignKey(User, on_delete=models.CASCADE)
	bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
	time_use = models.IntegerField()
	cost_of_rent = models.IntegerField()

