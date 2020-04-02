from django.db import models
from covid_gandaki.lb.models import Address, Person



class Family(models.Model):
    head = models.ForeignKey(Person, on_delete=models.CASCADE)
    member = models.ForeignKey(Person, related_name="member", blank=True, null=True, on_delete=models.SET_NULL)

class Needy (models.Model):
    # (छ) सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_of_need = models.CharField(max_length=300, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)







