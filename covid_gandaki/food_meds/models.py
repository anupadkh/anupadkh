from django.db import models
from viewflow.models import Process
from covid_gandaki.public.models import Person
from covid_gandaki.lb.models import Municipality


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
    qty = models.CharField(max_length=400)
    sufficiency = models.IntegerField(default=1)
    remarks = models.TextField(null=True, blank=True)
    demand_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Production(models.Model):
    # स्थानियतहमा उत्पादित तर बिक्रि हुन नसकी खेर गईरहेको वस्तुः
    name = models.CharField(max_length=300)
    qty = models.CharField(max_length=50)
    remarks = models.TextField()
    produced_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Medical(models.Model):
    # (च) तत्काल आवश्यक औषधि र मेडीकल उपकरण (PPE, मास्क, सेनिटाईजर, साबुन, थर्मोमिटर, पन्जा आदि) सम्वन्धि विवरण
    name = models.CharField(max_length=300)
    required_qty = models.CharField(max_length=50)
    remarks = models.TextField()
    available = models.CharField(max_length=50)
    produced_by = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Fulfilled(models.Model):
    name = models.CharField(max_length=50)
    obj_id = models.IntegerField()
    fulfilled_date = models.DateTimeField(auto_now_add=True)

