from django.forms import ModelForm
from covid_gandaki.lb.models import Municipality, Person2

class MunForm(ModelForm):
    class Meta:
        model = Municipality
        fields = '__all__'

class Person2Form(ModelForm):
    class Meta:
        model= Person2
        exclude = ['remarks','location','formtype', 'created']
    
    # def __init__(self,*args,**kwargs):
    #     super(Person2Form, self).__init__(*args, **kwargs)
    #     self.fields['age'].widget.attrs.update({'class': 'cell-6'})
    #     self.fields['mobile'].widget.attrs.update({'class': 'cell-6'})
    #     self.fields['current_address'].widget.attrs.update({'class': 'cell-md-6'})
    #     self.fields['permanent_address'].widget.attrs.update({'class': 'cell-md-6'})
    #     self.fields['full_name'].widget.attrs.update(
    #         {'class': 'cell-12'})
