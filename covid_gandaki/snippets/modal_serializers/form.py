from covid_gandaki.form.models import Travel
from covid_gandaki.public.models import Person
from covid_gandaki.lb.models import Address
from covid_gandaki.users.models import Employee
from rest_framework import serializers
from django.db import transaction
# from .public import Person

class Lb_Travel_Serializer(serializers.ModelSerializer):
    # user =
    name = serializers.CharField(write_only=True)
    age = serializers.IntegerField(write_only=True, allow_blank=True, allow_null=True)
    ward = serializers.IntegerField(write_only=True)
    gender = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Travel
        fields = "__all__"
        read_only_fields = ['created_date','created_by','traveller']
    
    @transaction.atomic
    def create(self,validated_data):
        if self.initial_data.get('id',False):
            instance = Travel.objects.get(id=self.initial_data['id'])
            traveller = instance.traveller
            mun = traveller.current_full_address.mun
            address = traveller.current_full_address
            
        else:
            request = self.context['request']
            emp_submitter = Employee.objects.get(user=request.user)
            # Employee.municipality = Office
            mun = emp_submitter.municipality.address.mun
            address = Address(mun=emp_submitter.municipality.address.mun)
            traveller = Person()
            instance = Travel(traveller=traveller)
            instance.created_by = request.user
            
        
        traveller.full_name = validated_data.get('name',traveller.full_name)
        traveller.age = validated_data.get('age', traveller.age)
        address.ward = validated_data.get(
            'ward', address.ward)
        address.save()
        traveller.current_full_address = address
        traveller.gender = validated_data.get('gender', traveller.gender)
        traveller.save()
        instance.traveller = traveller

        
        skip_fields = ['traveller', 'created_by']
        for attr, value in validated_data.items():
            if attr in skip_fields:
                continue

            try:
                setattr(instance, attr, value)
            except:
                pass

        instance.full_clean()
        instance.save()
        return instance
        
        
        

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['ward'] = obj.traveller.current_full_address.ward
        data['name'] = obj.traveller.full_name
        data['age'] = obj.traveller.age
        data['gender'] = obj.traveller.gender
        return data
        
        # Traveller = data['traveller']
        # Traveller = obj.traveller
        # # data['new'] = obj.traveller
        # add =Traveller.current_full_address
        # try:
        #     data['mun'] = add.mun.nep_name
        #     data['ward'] = add.ward
        #     data['district'] = add.mun.district.nep_name
        # except:
        #     data['mun'] = ''
        #     data['ward'] = ''
        #     data['district']=''
        # return data
    
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(Lb_Travel_Serializer, self).__init__(many=many, *args, **kwargs)
        
