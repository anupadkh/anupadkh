from covid_gandaki.food_meds.models import *
from rest_framework import serializers

class Lb_Food_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Food
        fields = ['name','qty','qty_unit','sufficiency','remarks']
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['order_type'] = 2
        return data
