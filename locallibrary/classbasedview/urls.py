from django.urls import path

from classbasedview.views.cbv.views import GreetingView,  MorningGreetingView, MyFormView
from classbasedview.views.cbv import views

#the simplest way of decorating class-based views is to decorate the result of the as_view() method. 
#The easiest place to do this is in the URLconf where you deploy your view:
from django.contrib.auth.decorators import login_required


urlpatterns = [
path('greeting/', 
	login_required(GreetingView.as_view())),
path('morninggreeting/',  MorningGreetingView.as_view()),
#checking clase-based view hangling POST requests
path('myform/', MyFormView.as_view()),
path('rest/',views.rest_team)

]