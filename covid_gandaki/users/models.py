from django.db import models
from django.contrib.auth.models import AbstractUser
from covid_gandaki.lb.models import Municipality

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    municipality = models.ForeignKey(Municipality,blank=True, null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

class Nepali(models.Model):
    appname = models.CharField(max_length=100)
    fieldname = models.CharField(max_length=100)
    nepali_name = models.CharField(max_length=300, blank=True, null=True)
