from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from classbasedview.forms import MyForm


class GreetingView(View):
	greeting = "Good Day"

	def get(self, request):
		return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
	greeting = "Morning to ya"




 #basic class-based view that handles forms may look something like this:

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


#rest testng
# views.py (In stores a
from classbasedview.models import Team
import json
def rest_team(request):
    team= Team(name='Dynamo', sport='tenis')
    team_names = [{"name":team.name} for team in object_list]
    return HttpResponse(json.dumps(team_names), content_type='application/json')
