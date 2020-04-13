from django import forms
from .models import Person2

class Person2Form(forms.ModelForm):

    class Meta:
        model = Person2
        fields = '__all__'
        widgets={'id': forms.HiddenInput()}
    
    
