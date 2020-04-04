from covid_gandaki.food_meds.models import *
from rest_framework import serializers
from covid_gandaki.users.models import Employee


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
        exclude = ['created','demand_by','created_by']
    
    def create(self, validated_data):
        self.created_by = self.context['request'].user
        employee = Employee.objects.get(user = self.created_by)
        self.demand_by = employee.municipality
        return super().create(validated_data)


class Lb_Production_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Production
        exclude = ['created','produced_by','created_by']

    def create(self, validated_data):
        self.created_by = self.context['request'].user
        employee = Employee.objects.get(user = self.created_by)
        self.produced_by = employee.municipality
        return super().create(validated_data)


class Lb_Medical_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Medical
        exclude = ['created','produced_by','created_by']
    
    def create(self, validated_data):
        self.created_by = self.context['request'].user
        employee = Employee.objects.get(user = self.created_by)
        self.produced_by = employee.municipality
        return super().create(validated_data)


class Lb_Fulfilled_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Fulfilled
        exclude = ['fulfilled_date']
