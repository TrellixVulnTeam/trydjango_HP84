# import Models from Django's mysql database
from django.db import models

# Create your models here.
# Creates a Product class, names it Product, and passes 
# models.Model so that we have model functionality
class Product(models.Model):
# Model fields get a name and an instruction on the type 
# and length of expected data 
	title = models.CharField(max_length=120) #max_length is essential for CharField
	#price = models.TextField()
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10000)
	summary = models.TextField()