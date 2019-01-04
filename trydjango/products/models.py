# import Models from Django's mysql database
from django.db import models

# Create your models here.
# Creates a Product class, names it Product, and passes 
# models.Model so that we have model functionality
class Product(models.Model):
# Model fields get a name and an instruction on the type 
# and length of expected data 
	title = models.TextField()
	description = models.TextField()
	price = models.TextField()