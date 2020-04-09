from django.db import models
from covid_gandaki.lb.models import Address, Hospital, Municipality
from covid_gandaki.users.models import User



class Person(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="Full Name")
    age = models.IntegerField(null=True, blank=True)
    permanent_address = models.CharField(max_length=500, null=True, blank=True)
    current_address = models.CharField(max_length=500, null=True, blank=True)
    mobile = models.CharField(
        max_length=300, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    permanent_full_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="Permanent")
    current_full_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="Temporary")
    belong_to_form = models.IntegerField(default=1) 
    # Type of Form Actually: 1 = Local Body, 3 = General Public, 4= ReliefFund
    gender = models.IntegerField(default=1, verbose_name='लिङ्ग')

    def __str__(self):
        return self.full_name
    class Meta:
        unique_together = ('mobile', 'belong_to_form',)

    def municipality(self):
        return self.current_full_address.mun

    def ward(self):
        return self.current_full_address.ward


class Family(models.Model):
    head = models.ForeignKey(Person, on_delete=models.CASCADE)
    member = models.ForeignKey(
        Person, related_name="member", blank=True, null=True, on_delete=models.SET_NULL)
    relation_type=models.IntegerField(default=0)


class Needy (models.Model):
    # (छ) सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_of_need = models.CharField(max_length=300, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now=True)
    municipality = models.ForeignKey(Municipality, blank=True, null=True, on_delete=models.CASCADE)


class QTPerson(models.Model):
    # (ग) COVID 19 टेस्ट सम्वन्धि विवरण
    person = models.ForeignKey(
        Person, on_delete=models.SET_NULL, null=True, blank=True)
    quarantined_zone = models.ForeignKey(
        Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    is_postive = models.BooleanField(default=False)
    remarks = models.TextField(
        verbose_name="Remarks", null=True, blank=True, max_length=300)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

