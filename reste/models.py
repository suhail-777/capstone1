from django.db import models
from django.contrib.auth.models import User

class addremainders(models.Model):
	name=models.CharField(max_length=50)
	date=models.DateField()
	description=models.CharField(max_length=100)

# Create your models here.
