from covid_gandaki.food_meds.models import *
from rest_framework import serializers


class Lb_Food_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Food
        fields = ['id', 'name', 'qty', 'qty_unit',
                  'sufficiency', 'remarks', 'ordered_by']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['order_type'] = 2
        return data


class Lb_Medicine_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Food
        exclude = ['created']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['order_type'] = 2
        return data


class Lb_Petroleum_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Petroleum
        exclude = ['created']


class Lb_Production_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Production
        exclude = ['created']


class Lb_Medical_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Medical
        exclude = ['created']


class Lb_Fulfilled_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Fulfilled
        exclude = ['fulfilled_date']
