from covid_gandaki.snippets.modal_serializers import lb, users, food_meds, public, form
import json
from django.conf import settings

from django.core.management.base import BaseCommand, CommandError




def generate_mun_list():
    mun_stat = {}
    try:
        mydir = settings.STATIC_ROOT
    except:
        mydir = settings.STATICFILES_DIRS[0]
    mun_stat['muns'] = list(lb.Municipality.objects.all().values())
    mun_stat['district'] = list(lb.District.objects.all().values())
    mun_stat['employees'] = list(users.Employee.objects.all().values('user__id', 'municipality__address__mun__id', 'id', 'municipality__id'))
    mun_stat['hospitals'] = lb.HospitalSerializer(lb.Hospital.objects.all(), many=True).data
    mun_stat['travellers'] = list(form.Travel.objects.all().values('created_by__id', 'created_office__id', 'Foreign Country', 'remarks', 'Arrival Date'))
    mun_stat['needy'] = list(public.Needy.objects.all().values('type_of_need', 'created_by', 'municipality__id', 'type_of_need'))
    mun_stat['quarantines'] = list(public.QTPerson.objects.all().values('quarantined_zone', 'is_positive', 'created_by'))
    mun_stat['food'] = list(food_meds.Petroleum.objects.all().values('name', 'qty_unit', 'qty', 'sufficiency', 'demand_by__id'))
    mun_stat['medicine'] = list(food_meds.Medical.objects.all().values('name', 'required_qty', 'qty_unit', 'available', 'produced_by__id', 'created_by__id' ))
    mun_stat['relief_packages'] = list(food_meds.FoodName.objects.all().values('name', 'mun__id', 'qty', 'unit', 'rate_equivalent'))
    mun_stat['production'] = list(food_meds.Production.objects.all().values('name', 'qty', 'produce_freq', 'qty_unit', 'produced_by__id', 'created_by__id'))
    with open( mydir + '/data_mun.json', 'w+') as f:
        f.write(json.dumps(mun_stat))
        f.close()
        pass
    
    mun_stat = {}
    mun_stat['public_food'] = list(food_meds.Food.objects.all().values('name', 'qty', 'qty_unit', 'sufficiency'))
    mun_stat['public_medicine'] = list(food_meds.Medicine.objects.all().values('name', 'qty', 'type_medicine', 'sufficiency'))

    with open(mydir + '/data_public.json', 'w+') as f:
        f.write(json.dumps(mun_stat))
        f.close()
        pass

    return True


class Command(BaseCommand):
    help = 'Generates the Data File for analytics'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        return generate_mun_list()
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS(
        #         'Successfully closed poll "%s"' % poll_id))
