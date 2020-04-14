from django.db import models

# Create your models here.

from covid_gandaki.public.models import Person,Address, Municipality
from covid_gandaki.users.models import User, Office

class Travel(models.Model):
    traveller = models.ForeignKey(Person, on_delete=models.CASCADE)
    nepal_arrival_date = models.TextField(
        verbose_name="नेपाल प्रवेश मिति", name="Arrival Date", blank=True, null=True)
    country_outside = models.CharField(
        verbose_name="बाहिर रहेको देश", name="Foreign Country", max_length=300)
    mode_of_transport_international = models.CharField(
        verbose_name="विदेशवाट नेपाल प्रवेश गर्दा प्रयोग गरेको यातायात साधन", max_length=100,null=True, blank=True)
    mode_of_transport_national = models.CharField(
        verbose_name="काठमाडौँ वा नाकावाट स्थानिय तहमा आउदा प्रयोग गरेको यातायात साधन", max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now=True
    )
    created_by = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    created_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True,null=True)

    

class Stat(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    image = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'ड्यासबोर्ड सेटिङ्ग र काउन्टर'
        verbose_name_plural = 'ड्यासबोर्डका काउन्टरहरु'

class StatValues(models.Model):
    reference = models.ForeignKey(Stat, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    value = models.CharField(null=True, blank=True, max_length=10)

    def __str__(self):
        return self.title
    
class StatCounters(models.Model):
    reference = models.ForeignKey(Stat, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    class_name = models.CharField(max_length=300)
    constraint = models.CharField(max_length=100)

class CovidCounters(models.Model):
    mun = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    no_person = models.BooleanField(
        default=0, null=True, blank=True, verbose_name="COVID-19 को CASE नभएको")
    samples = models.IntegerField(default=0, null=True, blank=True, verbose_name="सङ्कलित नमुना")
    infected = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="सङ्क्रमित")
    death = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="मृत्यु")
    cured = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="निको भएको")
    result_waiting = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="नतिजा आउन बाँकी")
    
