from covid_gandaki.form.models import *
from rest_framework import serializers


class Lb_Travel_Serializer(serializers.ModelSerializer):
    # user =
    traveller_name = serializers.CharField(source='traveller.full_name')
    traveller_age = serializers.CharField(source='traveller.age')
    
    class Meta:
        model = Travel
        exclude = ['created_date']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        # Traveller = data['traveller']
        Traveller = obj.traveller
        # data['new'] = obj.traveller
        add =Traveller.current_full_address
        try:
            data['mun'] = add.mun.nep_name
            data['ward'] = add.ward
            data['district'] = add.mun.district.nep_name
        except:
            data['mun'] = ''
            data['ward'] = ''
            data['district']=''
        return data
        
        
