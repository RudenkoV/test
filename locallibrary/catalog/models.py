from django.db import models

# Create your models here.


class Employee(models.Model):
    
	POSITIONS = (
	('JR', 'Junior'),
	('SR', 'Senior'),
	('GR', 'Graduate'),
	)
	employee = models.CharField(max_length=100)
	position = models.CharField(max_length=2, choices=POSITIONS)
	company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
	salary = models.CharField(max_length=100)

	def __str__(self):
		return self.employee


   



class Company(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name


class Country(models.Model):
	name = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)

	def __str__(self):
		return self.name





