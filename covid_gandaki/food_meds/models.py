from django.db import models
from viewflow.models import Process
from covid_gandaki.public.models import Person
from covid_gandaki.lb.models import Municipality
from covid_gandaki.users.models import User


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

class Food(models.Model):
    # खाद्यान्न, तरकारी, दुध, अण्डा, मासु) र पशुपंक्षिको दाना, ग्याँस, पेट्रोलियम पदार्थ
    name = models.CharField(max_length=300)
    qty = models.FloatField(default=0.0)
    qty_unit = models.CharField(max_length=300)
    sufficiency = models.IntegerField(default=1)
    ordered_by = models.IntegerField()
    order_type = models.IntegerField(default=1) # 1=Person, 2=LB
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

class Medicine(models.Model):
    name = models.CharField(max_length=150)
    type_medicine = models.CharField(max_length=150)
    qty = models.CharField(max_length=400)
    sufficiency = models.IntegerField(default=1)
    ordered_by = models.IntegerField()
    order_type = models.IntegerField(default=1)  # 1=Person, 2=LB
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    mode_delivery = models.IntegerField(default=1)

class Petroleum(models.Model):
    name = models.CharField(max_length=300)
    qty_unit = models.CharField(max_length=160, default='वटा')
    qty = models.CharField(max_length=400)
    sufficiency = models.IntegerField(default=1)
    remarks = models.TextField(null=True, blank=True)
    demand_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Production(models.Model):
    # स्थानियतहमा उत्पादित तर बिक्रि हुन नसकी खेर गईरहेको वस्तुः
    name = models.CharField(max_length=300)
    qty = models.CharField(max_length=50)
    produce_freq = models.CharField(max_length=50, default='daily', blank=True, null=True)
    qty_unit = model.CharField(max_length=70, default="केजी")
    remarks = models.TextField()
    produced_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Medical(models.Model):
    # (च) तत्काल आवश्यक औषधि र मेडीकल उपकरण (PPE, मास्क, सेनिटाईजर, साबुन, थर्मोमिटर, पन्जा आदि) सम्वन्धि विवरण
    name = models.CharField(max_length=300)
    required_qty = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    qty_unit = models.CharField(max_length=80)
    available = models.CharField(max_length=50, null=True, blank=True)
    produced_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Fulfilled(models.Model):
    name = models.CharField(max_length=50)
    obj_id = models.IntegerField()
    fulfilled_date = models.DateTimeField(auto_now_add=True)

class FoodName(models.Model):
    name = models.CharField(max_length=100)
    mun = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.CharField(max_length=50)
    rate_equivalent = models.FloatField(default=0.0)

    def __str__(self):
        return "%s (%s)" % (self.name, self.unit)

