from rest_framework import serializers
from covid_gandaki.lb.models import District, Municipality, Hospital, CovidCases, Person2, OfficeEmployee
from covid_gandaki.public.models import Person, Family
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


    class Meta:
        model = Hospital
        fields = '__all__'



class CovidCasesSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CovidCases
        fields = '__all__'

from covid_gandaki.lb.sub_models.rahat import ReliefFund


from collections import OrderedDict

class ReliefFundSerializer(serializers.ModelSerializer):
    receiver_name = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    father_name = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    grandfather_name = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    mobile = serializers.CharField(
        required=False, allow_blank=True, max_length=300)
    receiver_address = serializers.CharField(
        required=False, allow_blank=True, max_length=300)

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['receiver_name'] = obj.receiver.full_name
        data["submitter_name"] = obj.submitter.full_name
        data['office_name'] = obj.office.name
        data['office_mun'] = obj.office.address.mun.nep_name
        data['office_ward'] = obj.office.address.ward
        data['receiver_mobile'] = obj.receiver.mobile
        family = Family.objects.filter(head=obj.receiver)
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
        
        data['submitter_mobile'] = obj.submitter.mobile
        data['receiver_address'] = obj.receiver.permanent_address
        return data
    
    

    @transaction.atomic
    def create(self, validated_data):
        # print('We Entered Here')
        # if self.initial_data.get('id',False):
        #     return self.update(instance=self, validated_data=validated_data)
        flag = {'father':0,'grandfather':0}

        if self.initial_data.get('id',False):
            instance = ReliefFund.objects.get(id=self.initial_data['id'])
            head = instance.receiver
            
            try:
                father = Family.objects.get(head=head, relation_type=1)
                try:
                    grandfather = Family.objects.get(
                        head=head, relation_type=2).member
                except:
                    grandfather = Person()
                    flag['grandfather']=1
                    
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

        father.full_name = validated_data['father_name']
        grandfather.full_name = validated_data['grandfather_name']
        head.full_name = validated_data['receiver_name']
        head.mobile = validated_data['mobile']
        head.permanent_address = validated_data['receiver_address']
        head.belong_to_form = 2
        head.save()
        father.save()
        grandfather.save()

        # Only save for New Members for the families
        if (flag['father'] == 1) :   
            family = Family(head=head, member=father, relation_type=1)
            family.save()
        elif (flag['grandfather']==1):
            family = Family(head=head, member=grandfather, relation_type=2)
            family.save()
        

        # validated_data['receiver'] = head
        # validated_data['submitter_id'] = submitter_id #already present in create
        submitter = validated_data['submitter']
        office = OfficeEmployee.objects.get(employee=submitter).office
        if self.initial_data.get('id', False):
            instance.receiver = head
            instance.submitter = submitter
            instance.office = office
            instance.relief_details = validated_data['relief_details']
            instance.save()
            return instance
        return ReliefFund.objects.create(receiver=head, submitter=submitter,office=office,relief_details=validated_data['relief_details'])


    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     print(instance.receiver.full_name)
    #     head = instance.receiver
    #     head.full_name = validated_data.get('receiver_name', head.full_name)
    #     head.mobile = validated_data.get(
    #         'mobile', head.mobile)
    #     head.permanent_address = validated_data.get(
    #         'receiver_address', head.permanent_address)
    #     head.belong_to_form = 2
    #     head.save()

    #     try:
    #         father = Family.objects.get(head=head, relation_type=1)
    #         father.full_name = validated_data.get('father_name', father.full_name)
    #         father.belong_to_form = 2
    #         father.save()
    #     except:
    #         try:
    #             father = Person(full_name=validated_data.get('father_name'))
    #             father.belong_to_form = 2
    #             father.save()
    #         except:
    #             pass

    #     try:
    #         grandfather = Family.objects.get(head=head, relation_type=2)
    #         grandfather.full_name = validated_data.get(
    #             'grandfather_name', grandfather.full_name)
    #         grandfather.belong_to_form = 2
    #         grandfather.save()
    #     except:
    #         try:
    #             grandfather = Person(full_name=validated_data.get('grandfather_name'))
    #             grandfather.belong_to_form = 2
    #             grandfather.save()
    #         except:
    #             pass
        
    #     instance.relief_details = validated_data.get('relief_details', instance.relieve_details)
    #         #         validated_data is an OrderedDict and OrderedDict.get(key, default) is the method that fetches the value for the given key, returning the default if the key is missing from the dict.


    #         # In other words: instance.title = validated_data.get('title', instance.title) will try to fetch title from validated_data but will return the current instance.title if the title key is not present in the validated data.
    #     instance.save()
    #     return instance

    class Meta:
        model = ReliefFund
        fields = '__all__'

    
