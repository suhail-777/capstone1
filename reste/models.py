from django.db import models
from django.contrib.auth.models import User

class Remainders(models.Model):
	name=models.CharField(max_length=50)
	date=models.DateField()
	description=models.CharField(max_length=100)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
