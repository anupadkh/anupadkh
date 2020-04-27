from covid_gandaki.snippets.modal_serializers import lb, users, food_meds, public, form
import json
from django.conf import settings

from covid_gandaki.form.models import Stat, StatCounters, StatValues
from django_q.tasks import async_task, schedule
from django_q.models import Schedule

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


def dash_generate():
    data = []
    y = Stat.objects.all()
    for m in y:
        values = []
        for z in StatValues.objects.filter(reference=m):
            values.append({
                'title': z.title,
                'value': z.value
            })
        for z in StatCounters.objects.filter(reference=m):
            App = eval(z.class_name)
            constraint = eval(z.constraint)
            count = App.objects.filter(**constraint).count()
            values.append({
                'title': z.title,
                'value': count
            })

        data.append({
            "title": m.title,
            "subtitle": m.subtitle,
            "image": m.image,
            "values": values,
        })

        with open(settings.STATICFILES_DIRS[0] + '/data1.json', 'w+') as f:
            f.write(json.dumps(data))
            f.close()
            pass

        if settings.DEBUG == False:
            async_task(generate_mun_list)

        else:
            async_task(generate_mun_list)

        # if settings.DEBUG == False:
        #     process = subprocess.run(
        #         ["python" , settings.BASE_DIR+ "/manage.py", "report_generate"], stdout=subprocess.PIPE)
        # else:
        #     # process1 = Popen(["python", settings.BASE_DIR + "/production_manage.py", "report_generate"],
        #     #                 bufsize=0, cwd=settings.BASE_DIR, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        #     process = subprocess.run(
        #         ["python", settings.BASE_DIR + "/production_manage.py", "report_generate"], stdout=subprocess.PIPE)
        #     # generate_mun_list()
        return True


class Command(BaseCommand):
    help = 'Generates the Data File for analytics'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        if Schedule.objects.count() == 0:
            schedule(dash_generate,schedule_type=Schedule.HOURLY)
        self.stdout.write('Added Successfully the dashboard tasks')
        
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS(
        #         'Successfully closed poll "%s"' % poll_id))
