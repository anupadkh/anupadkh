from rest_framework import serializers
from covid_gandaki.public.models import Person, Address,Family, Needy, QTPerson


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

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['full_name'] = obj.name.full_name
        data['age'] = obj.name.age
        return data

    class Meta:
        model = Needy
        fields = '__all__'


class QTPersonSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['full_name'] = obj.person.full_name
        data['age'] = obj.person.age

        try:
            data['ward'] = obj.current_full_address.ward
        except:
            data['ward'] = ''

        data['hospital_name'] = obj.quarantined_zone.name
        return data

    class Meta:
        model = QTPerson
        fields = '__all__'
