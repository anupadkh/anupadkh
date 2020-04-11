from django import forms
from .models import Person2

class Person2Form(forms.ModelForm):
    pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Person2
        fields = '__all__'
    
    
