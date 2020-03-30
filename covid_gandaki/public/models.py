from django.db import models


class Address(models.Model):
    street = models.CharField(null=True, blank=True, max_length=300)
    ward = models.IntegerField(default=1)
    mun = models.CharField(max_length=300)
    house_no = models.CharField(null=True, blank=True, max_length=50)
    district = models.CharField(max_length=300, name="District")

    def __str__(self):
        return("%s - %s, %s - %s, %s"%(self.street, self.house_no, self.mun, self.ward, self.district))


class Person(models.Model):
    full_name = models.CharField(max_length=300, name="Full Name")
    age = models.IntegerField(name="Age", null=True, blank=True)
    permanent_address = models.CharField (max_length=500, null=True, blank=True)
    current_address = models.CharField(max_length=500, null=True, blank=True)
    mobile = models.CharField(max_length=300, null=True, blank=True)
    remarks = models.TextField(blank=True,null=True)
    created = models.DateField(auto_now=True)
    # permanent_address = models.ForeignKey(Address,on_delete=models.SET_NULL, null=True, blank=True, related_name="Permanent")
    # current_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="Temporary")

    def __str__(self):
        return self.full_name

class Family(models.Model):
    head = models.ForeignKey(Person, on_delete=models.CASCADE)
    member = models.ForeignKey(Person, related_name="member", blank=True, null=True, on_delete=models.SET_NULL)

class Needy (models.Model):
    # (छ) सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_of_need = models.CharField(max_length=300, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)





