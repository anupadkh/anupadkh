from django.db import models
from covid_gandaki.public.models import Address, Person

# Create your models here.
class District(models.Model):
    district_name = models.CharField(max_length=300, blank=True, null=True)
    nep_name = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nep_name

class Municipality(models.Model):
    mun_name = models.CharField(max_length=300)
    nep_name = models.CharField(max_length=300, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    chairman = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True, related_name="chair")
    deputy_chairman = models.ForeignKey(
        Person, on_delete=models.SET_NULL, blank=True, null=True, related_name="deputy_chair")
    administrator = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True, related_name="admin")

    def __str__(self):
        if self.nep_name:
            return self.nep_name
        else:
            return self.mun_name

    

class Hospital(models.Model):
    name = models.CharField(max_length=300)
    # address = models.CharField(max_length=400)
    total_beds = models.IntegerField(default=1)
    mun = models.ForeignKey(Municipality, on_delete=models.SET_NULL, blank=True, null=True)
    ward = models.IntegerField(default=1)
    is_quarantine = models.IntegerField(default=1)  # Not a quarantine zone, Is a quarantine zone, Is an isolation zone
    currently_quarantined = models.IntegerField(default=0)  # हाल क्वारेन्टाइनमा बसेकाहरुको संख्या

    def __str__(self):
        return self.name

class QTPerson(models.Model):
    # (ग) COVID 19 टेस्ट सम्वन्धि विवरण
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    quarantined_zone = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    is_postive = models.BooleanField(default=False)
    remarks = models.TextField(verbose_name="Remarks", null=True, blank=True, max_length=300)


class CovidCases(models.Model):
    mun = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    positive_cases = models.IntegerField(default=0) # 1 for positive
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, blank=True, null=True)


