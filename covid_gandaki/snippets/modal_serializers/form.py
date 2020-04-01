from covid_gandaki.form.models import *
from rest_framework import serializers


class Lb_Travel_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Travel
        exclude = ['created_date']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        
