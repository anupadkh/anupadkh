from rest_framework import serializers
from covid_gandaki.public.models import Person, Address,Family, Needy


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
    class Meta:
        model = Needy
        fields = '__all__'
