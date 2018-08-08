from django.urls import path



from . import views
from catalog.views.cbv.CreateView import CreateCountry



urlpatterns = [

#path('', views.emp, name='index'),
#path('home/', views.home, name='home'),
path('create_country/', CreateCountry.as_view(), name='create_country'),
]

