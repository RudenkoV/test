from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


from .forms import EmployeeForm






def home(request):
    return render(request,'home.html') 


def emp(request):
	if request.method == "POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home/')    
	else:  
		form = EmployeeForm()  
	return render(request,'index.html',{'form':form}) 


#from django.views.generic.edit import CreateView
#from catalog.models import Country

#class CreateCountry(CreateView):
    #model = Country
    #fields = ['name']

