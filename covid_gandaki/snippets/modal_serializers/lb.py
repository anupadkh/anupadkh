from rest_framework import serializers
from covid_gandaki.lb.models import District, Municipality, Hospital, QTPerson, CovidCases


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class QTPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = QTPerson
        fields = '__all__'


class CovidCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCases
        fields = '__all__'
