from django import forms
from .models import CovidCounters


class CounterCovidForm(forms.ModelForm):

    class Meta:
        model = CovidCounters
        fields = '__all__'
        widgets = {'id': forms.HiddenInput(),
        'mun': forms.HiddenInput()}
