from django.db import models

# Create your models here.

from covid_gandaki.public.models import Person,Address

class Travel(models.Model):
    traveller = models.ForeignKey(Person, on_delete=models.CASCADE)
    nepal_arrival_date = models.DateField(
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

