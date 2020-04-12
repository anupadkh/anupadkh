from covid_gandaki.food_meds.models import *
from rest_framework import serializers
from covid_gandaki.users.models import Employee


class Lb_Food_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Food
        fields = ['id', 'name', 'qty', 'qty_unit',
                  'sufficiency', 'remarks', 'ordered_by']
        read_only_fields =['demand_by','created_by']
    

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['order_type'] = 2
        return data


class Lb_Medicine_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Food
        exclude = ['created']
        read_only_fields =['produced_by']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['order_type'] = 2
        return data


class Lb_Petroleum_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Petroleum
        fields = "__all__"
        read_only_fields = ['created','demand_by','created_by']
    
    def create(self, validated_data):
        request = self.context['request']
        emp_submitter = Employee.objects.get(user=request.user)
        mun = emp_submitter.municipality.address.mun
        if self.initial_data.get('id',False) == False:
            instance = Petroleum()
            instance.demand_by = mun
            instance.created_by = request.user
        else:
            instance = Petroleum.objects.get(id=self.initial_data['id'])
        
        instance.name = validated_data.get('name',instance.name)
        instance.qty = validated_data.get('qty', instance.qty)
        instance.qty_unit = validated_data.get('qty_unit', instance.qty_unit)
        instance.sufficiency = validated_data.get('sufficiency', instance.sufficiency)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.save()
        
        return instance
        


class Lb_Production_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Production
        write_only_fields = ['created','created_by']
        fields = "__all__"
        read_only_fields = ['produced_by']

    def create(self, validated_data):
        request = self.context['request']
        emp_submitter = Employee.objects.get(user=request.user)
        mun = emp_submitter.municipality.address.mun
        if self.initial_data.get('id',False) == False:
            instance = Production()
            instance.produced_by = mun
            instance.created_by = request.user
        else:
            instance = Production.objects.get(id=self.initial_data['id'])
        
        instance.name = validated_data.get('name',instance.name)
        instance.qty = validated_data.get('qty', instance.qty)
        instance.qty_unit = validated_data.get('qty_unit', instance.qty_unit)
        instance.remarks = validated_data.get('remarks',instance.remarks)
        instance.produce_freq = validated_data.get('produce_freq', instance.produce_freq)        
        instance.save()
        return instance


class Lb_Medical_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Medical
        read_only_fields = ['created','produced_by','created_by']
        fields = "__all__"

    
    def create(self, validated_data):
        request = self.context['request']
        emp_submitter = Employee.objects.get(user=request.user)
        mun = emp_submitter.municipality.address.mun
        if self.initial_data.get('id',False) == False:
            instance = Medical()
            instance.produced_by = mun
            instance.created_by = request.user
            
        else:
            instance = Medical.objects.get(id=self.initial_data['id'])
        
        instance.name = validated_data.get('name',instance.name)
        instance.required_qty = validated_data.get('required_qty', instance.required_qty)
        instance.remarks = validated_data.get('remarks',instance.remarks)
        instance.available = validated_data.get('available', instance.available)
        instance.qty_unit = validated_data.get('qty_unit', instance.qty_unit)
        instance.save()
        return instance


class Lb_Fulfilled_Serializer(serializers.ModelSerializer):
    # user =
    class Meta:
        model = Fulfilled
        exclude = ['fulfilled_date']

class Lb_FoodName(serializers.ModelSerializer):
    class Meta:
        model = FoodName
        read_only_fields = ['mun']
        fields = "__all__"
    
    def create(self, validated_data):
        request = self.context['request']
        if self.initial_data.get('id',False) == False:
            instance = FoodName.objects.create(**validated_data)
            emp_submitter = Employee.objects.get(user=request.user)
            instance.mun = emp_submitter.municipality.address.mun
            instance.save()
        else:
            obj = FoodName.objects.get(id=self.initial_data['id'])
            obj.rate_equivalent = validated_data.get('rate_equivalent', obj.rate_equivalent)
            obj.name = validated_data.get('name', obj.name)
            obj.unit = validated_data.get('unit', obj.unit)
            
            instance = obj
            
        return instance
        
        
