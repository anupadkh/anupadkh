from covid_gandaki.form.models import *
from rest_framework import serializers


class Lb_Travel_Serializer(serializers.ModelSerializer):
    full_name = serializers.RelatedField('traveller.full_name')
    age = serializers.RelatedField('traveller.age')
    mun = serializers.RelatedField('traveller.mun')
    ward = serializers.RelatedField('traveller.ward')
    
    class Meta:
        model = Travel
        exclude = ['created_date']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        
