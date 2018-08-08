from django import forms

from .models import Team


class MyForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
