from django.db import models
from django.contrib.auth.models import AbstractUser
from covid_gandaki.lb.models import Municipality, Office

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def full_name(self):
        return self.first_name + " "+ self.last_name

    # def save(self, *args, **kwargs):
    #     new_user = super(User, self).save(*args, commit=False)
    #     self.set_password(self.password)

class Employee(models.Model):
    municipality = models.ForeignKey(
        Office, blank=True, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Nepali(models.Model):
    appname = models.CharField(max_length=100)
    fieldname = models.CharField(max_length=100)
    nepali_name = models.CharField(max_length=300, blank=True, null=True)
