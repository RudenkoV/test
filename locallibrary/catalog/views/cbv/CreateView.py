from django.views.generic.edit import CreateView
from catalog.models import Country

class CreateCountry(CreateView):
    model = Country
    fields = ['name']
