from rest_framework import serializers
from covid_gandaki.lb.models import District, Municipality, Hospital, CovidCases, Person2, OfficeEmployee, Office, Address
from covid_gandaki.public.models import Person, Family
from covid_gandaki.users.models import User, Employee
from covid_gandaki.food_meds import models as food_meds
from covid_gandaki.lb.sub_models import rahat
from django.db import transaction

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):


    def to_representation(self, obj):
        data = super().to_representation(obj)
        Quarantines = CovidCases.objects.filter(positive_cases=0).count()
        Covids = CovidCases.objects.filter(positive_cases=1).count()
        data['quarantine_count'] = Quarantines
        data['covid_count'] = Covids
        return data
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        request = self.context['request']
        employee = Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun # municipality refers to office actually
        instance.mun = mun
        instance.save()
        return instance        


    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ['mun']




class CovidCasesSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CovidCases
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    ward = serializers.IntegerField(write_only=True)
    street = serializers.CharField(max_length=300, write_only=True, allow_null=True, allow_blank = True)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ward'] = instance.address.ward
        data['municipality'] = instance.address.mun.mun_name
        data['street'] = instance.address.street
        return data
    
     
    
    def create(self, validated_data):
        request = self.context['request']
        employee = Employee.objects.get(user=request.user)
        # municipality refers to office actually
        mun = employee.municipality.address.mun
        with transaction.atomic():
        # try:
            request = self.context['request']
            if self.initial_data.get('id', False) != False:
                obj = Office.objects.get(id=self.initial_data['id'])
                address = obj.address
                
            else:
                obj = Office()
                address = Address(mun = mun)
            
            address.ward = validated_data.pop('ward')
            address.street = validated_data.pop('street')    
            address.save()
            obj.address = address
            obj.name = validated_data.get('name', obj.name)
            obj.description = validated_data.get('description', obj.description)
            obj.save()
        
        return obj

            
        #     return super().create(validated_data)
        # except:
        #     pass
    
    class Meta:
        model = Office
        fields = '__all__'
        read_only_fields = ['address']


class OfficeEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeEmployee
        fields = '__all__'

from covid_gandaki.lb.sub_models.rahat import ReliefFund, ReliefItem


from collections import OrderedDict

class ReliefFundSerializer(serializers.ModelSerializer):
    submitter_name = serializers.CharField(max_length=300, write_only=True)
    mobile = serializers.CharField(allow_null=True, allow_blank=True, write_only=True, max_length=10, min_length=10)
    address = serializers.CharField(max_length=300, write_only=True, allow_null = True)


    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['submitter_name'] = obj.submitter.full_name
        data['mobile'] = obj.submitter.mobile
        data['address'] = obj.submitter.current_address
        return data

    

    @transaction.atomic
    def create(self, validated_data):
        request = self.context['request']
        employee = Employee.objects.get(user=request.user)
        if self.initial_data.get('id', False):
            instance = ReliefFund.objects.get(id=self.initial_data['id'])
        else:
            default = Office.objects.filter(address__mun = employee.municipality.address.mun)[0]
            instance = ReliefFund(office = validated_data.get('office', default))
            instance.submitter = Person2()
        
        
        instance.submitter.full_name = validated_data.get('submitter_name', instance.submitter.full_name)
        instance.submitter.mobile = validated_data.get('mobile', instance.submitter.mobile)
        instance.submitter.current_address = validated_data.get('address', instance.submitter.current_address)
        submitter = instance.submitter
        # Throws error if the mobile number repeats
        submitter.save()
        instance.submitter = submitter
        instance.office = validated_data.get('office', instance.office)
        instance.save()
        return instance

    class Meta:
        model = ReliefFund
        exclude = ['submitter']


class ReliefPersonSerializer(serializers.ModelSerializer):
    father_name = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    grandfather_name = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    mobile = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    # reliefs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    submitter = serializers.IntegerField(write_only=True)

    class Meta:
        model = Person
        fields = "__all__"
        # extra_fields = ['receiver']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['mobile'] = obj.mobile
        family = Family.objects.filter(head=obj)
        try:
            father = family.get(relation_type=1).member
            data['father_name'] = father.full_name
        except:
            data['father_name'] = ''

        try:
            grandfather = family.get(relation_type=2).member
            data['grandfather_name'] = grandfather.full_name
        except:
            data['grandfather_name'] = ''
        try:
            fooditems = food_meds.FoodName.objects.filter(mun=obj.current_full_address.mun)
            for item in fooditems:
                data[item.id] = 0
                try:
                    rel_item = rahat.ReliefItem.objects.get(
                        receiver=obj, food_type=item)
                    data[item.id] = rel_item.qty
                except:
                    pass
        except:
            data['error'] = "error loading fooditems"
        return data
    
    # def get_relief_items(self, request):
    #     request = self.context['request']
    #     employee = Employee.objects.get(user=request.user)
    #     mun = employee.municipality.address.mun
    #     fooditems = food_meds.FoodName.objects.filter(mun=mun)
    #     for item in fooditems:
    #         data[item.id] = 0
    #         try:
    #             rel_item = rahat.ReliefItem.objects.get(
    #                 receiver=obj, food_type=item)
    #             data[rel_item.id] = rel_item.qty
    #         except:
    #             pass

    def create(self, validated_data):
        flag = {'father': 0, 'grandfather': 0}

        if self.initial_data.get('id', False):
            head = Person.objects.get(id=self.initial_data['id'])
            try:
                father = Family.objects.get(head=head, relation_type=1)
                try:
                    grandfather = Family.objects.get(
                        head=head, relation_type=2).member
                except:
                    grandfather = Person()
                    flag['grandfather'] = 1
            except:
                father = Person()
                flag['father'] = 1
                try:
                    grandfather = Family.objects.get(
                        head=head, relation_type=2).member
                except:
                    grandfather = Person()
                    flag['grandfather'] = 1

        else:
            head = Person()
            father = Person()
            grandfather = Person()
            flag['father'] = 1
            flag['grandfather'] = 1

        father.full_name = validated_data['father_name']
        grandfather.full_name = validated_data['grandfather_name']
        head.full_name = validated_data['full_name']
        head.mobile = validated_data['mobile']
        head.permanent_address = validated_data['permanent_address']
        head.belong_to_form = 4
        user = self.context['request'].user
        employee = Employee.objects.get(user=user)
        head.current_full_address = employee.municipality.address
        with transaction.atomic():
            head.save()
            father.save()
            grandfather.save()

            # Only save for New Members for the families
            if (flag['father'] == 1):
                family = Family(head=head, member=father, relation_type=1)
                family.save()
            if (flag['grandfather'] == 1):

                family = Family(head=head, member=grandfather, relation_type=2)
                family.save()
        # foods = food_meds.FoodName.objects.filter(mun=head.current_full_address.mun)
        # validated_data = self.initial_data
        # RelFund = ReliefFund.objects.get(submitter = validated_data.get('submitter'))
        # for items in foods:
        #     RelItem, RelCreate = ReliefItem.objects.get_or_create(receiver=head, food_type=items, fund=RelFund)
        #     # RelItem.qty = validated_data.get(items.id)
        #     RelItem.save()
        return head


class ReliefItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefItem
        fields="__all__"
    


