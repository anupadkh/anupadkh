from django.db import models
from covid_gandaki.lb.models import Person2, Office
from covid_gandaki.public.models import Person
from covid_gandaki.food_meds.models import FoodName

class ReliefFund(models.Model):
    # List of Distributors (For Managing Submittors)
    submitter = models.ForeignKey(
        Person2, on_delete=models.SET_NULL, null=True, blank=True, 
        related_name='submittor')
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s - %s"%(self.submitter,self.office)
    

class ReliefItem(models.Model):
    fund = models.ForeignKey(ReliefFund, on_delete=models.CASCADE)
    qty = models.FloatField(default=0)
    # food_type = models.ForeignKey(FoodName, on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        Person, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='receiver')
