from django.forms import ModelForm
from .models import Employee, Country
from django import forms

# Create the form class.
class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['employee', 'position', 'company', 'salary']

