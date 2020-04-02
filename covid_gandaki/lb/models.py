from django.db import models




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
    chairman = models.IntegerField(blank=True,null=True)
    deputy_chairman = models.IntegerField(blank=True, null=True)
    administrator = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.nep_name:
            return self.nep_name
        else:
            return self.mun_name


class Address(models.Model):
    street = models.CharField(null=True, blank=True, max_length=300)
    ward = models.IntegerField(default=1)
    mun = models.ForeignKey(
        Municipality, on_delete=models.SET_NULL, blank=True, null=True)
    house_no = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return("%s - %s, %s - %s, %s" % (self.street, self.house_no, self.mun, self.ward, self.district))

class Person(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="Full Name")
    age = models.IntegerField(null=True, blank=True)
    permanent_address = models.CharField(max_length=500, null=True, blank=True)
    current_address = models.CharField(max_length=500, null=True, blank=True)
    mobile = models.CharField(
        max_length=300, null=True, blank=True, unique=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    permanent_full_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="Permanent")
    current_full_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="Temporary")

    def __str__(self):
        return self.full_name

    def municipality(self):
        return self.current_full_address.mun

    def ward(self):
        return self.current_full_address.ward



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


