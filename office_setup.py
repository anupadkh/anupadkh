from covid_gandaki.lb.models import Municipality,Office, Address                                                                                                    
muns = Municipality.objects.all()

def populate():
    for x in muns:
        y = Address(ward=1, mun = x)

        y.save()
        z = Office(name = x.mun_name + 'को कार्यालय', address=y)
        z.save()
