from django.db import models
from covid_gandaki.lb.models import Person2, Office
from covid_gandaki.public.models import Person

class ReliefFund(models.Model):
    receiver = models.ForeignKey(
        Person, on_delete=models.SET_NULL, null=True, blank=True, 
        related_name='receiver')
    submitter = models.ForeignKey(
        Person2, on_delete=models.SET_NULL, null=True, blank=True, 
        related_name='submittor')
    office = models.OneToOneField(Office, on_delete=models.SET_NULL, null=True, blank=True)
    relief_details = models.TextField()
