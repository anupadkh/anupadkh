from rest_framework import serializers
from covid_gandaki.lb.models import District, Municipality, Hospital, CovidCases
from covid_gandaki.public.models import Person


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
