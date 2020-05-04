from rest_framework import serializers
from covid_gandaki.public.models import Person, Address,Family, Needy, QTPerson
from covid_gandaki.lb.models import Hospital
from covid_gandaki.users.models import Employee
from django.db import transaction

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class NeedySerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=300, write_only=True)
    age = serializers.IntegerField(write_only=True)
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['full_name'] = obj.person.full_name
        data['age'] = obj.person.age
        return data
    
    @transaction.atomic
    def create(self, validated_data):
        if self.initial_data.get('id',False) == False :
            request = self.context['request']
            emp_submitter = Employee.objects.get(user=request.user)
            address = Address(mun=emp_submitter.municipality.address.mun, ward=validated_data.get('ward',1))
            address.save()
            person = Person(full_name=validated_data.get('full_name',''), age=validated_data.get('age'))
            person.save()
            # validated_data['person'] = person
            # validated_data['created_by']= emp_submitter.user
            # validated_data['municipality'] = emp_submitter.municipality.address.mun
            instance = Needy()
            instance.person = person
            instance.created_by = emp_submitter.user
            instance.municipality = emp_submitter.municipality.address.mun
        else:
            instance = Needy.objects.get(pk=self.initial_data['id'])
            needy = instance.person
            needy.age = validated_data.get('age',needy.age)
            needy.full_name = validated_data.get('full_name',needy.full_name)
            needy.save()
            # validated_data['person']=needy 
            # remove_fields = ['municipality','created_by','create_date']
            # for x in remove_fields:
            #     try:
            #         validated_data.pop(x)
            #     except:
            #         pass
            
            instance.person = needy
            instance.type_of_need = validated_data['type_of_need']
            instance.remarks = validated_data['remarks']
        
        instance.save()

        return instance

    class Meta:
        model = Needy
        fields='__all__'
        read_only_fields=['create_date', 'person']


class QTPersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=300, write_only=True)
    age = serializers.IntegerField( write_only=True)
    ward =serializers.IntegerField( write_only=True)
    gender = serializers.IntegerField(write_only=True, allow_null=True)
    
    

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['name'] = obj.person.full_name
        data['age'] = obj.person.age
        data['gender'] = obj.person.gender
        try:
            employee = Employee.objects.get(user=obj.created_by)
            data['mun'] = employee.municipality.address.mun.id
        except:
            pass

        try:
            data['ward'] = obj.person.current_full_address.ward
        except:
            data['ward'] = ''
        try:
            data['hospital_name'] = obj.quarantined_zone.name
        except:
            data['hospital_name'] = ""
        return data
    
    @transaction.atomic
    def create(self, validated_data):
        if self.initial_data.get('id',False):
            instance = QTPerson.objects.get(id=self.initial_data['id'])
            infected = instance.person
            address = infected.current_full_address

        else:
            request = self.context['request']
            instance = QTPerson()
            infected = Person()
            emp_submitter = Employee.objects.get(user=request.user)
            instance.created_by = emp_submitter.user
            # Employee.municipality = Office
            mun = emp_submitter.municipality.address.mun
            address = Address(mun=emp_submitter.municipality.address.mun)

        
        infected.full_name = validated_data.get('name',infected.full_name)
        infected.age = validated_data.get('age', infected.age)
        address.ward = validated_data.get(
            'ward', address.ward)
        address.save()
        infected.current_full_address = address
        infected.gender = validated_data.get('gender', infected.gender)
        infected.save()
        instance.person = infected
        
        skip_fields = ['person', 'created_by']
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




    class Meta:
        model = QTPerson
        fields = '__all__'
        read_only_fields = ["created_by","person"]
