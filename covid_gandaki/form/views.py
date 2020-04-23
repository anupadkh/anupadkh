from django.conf import settings
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from covid_gandaki.food_meds.models import *
from covid_gandaki.form.models import *
from covid_gandaki.lb.models import *
from covid_gandaki.public.models import *
from covid_gandaki.users.models import *
from covid_gandaki.users.forms import MunForm, Person2Form
from covid_gandaki.form.forms import CounterCovidForm, CovidCounters
from covid_gandaki.lb.sub_models.rahat import *
from pprint import pprint
from covid_gandaki.snippets.modal_serializers import lb, users, food_meds, public

from covid_gandaki.form.report_generate import generate_mun_list

if settings.DEBUG == False:
    from django_q.tasks import async_task, schedule

# Create your views here.
# @login_required(login_url='users:login')

from django.db import transaction

def index(request):
    # return render(request, 'polls/detail.html', {'question': question})
    return render(request, 'form/index.html', context={})
    return HttpResponse('Hello')

@login_required(login_url="users:login")
def lb_index(request):
    employee = Employee.objects.get(user=request.user)
    mun = employee.municipality.address.mun
    message=""
    covid_instance, status = CovidCounters.objects.get_or_create(mun=mun)
    covid_form = CounterCovidForm(instance=covid_instance)
    if request.method=="POST":
        data = request.POST
        if data['submit'] == 'covid':
            covid_form = CounterCovidForm(data, instance=covid_instance)
            if covid_form.is_valid():
                covid_instance = covid_form.save()
            
        else:
            with transaction.atomic():
                    if data['submit'] == 'chair':
                        man = Person2Form(data, instance = mun.chairman)
                        if man.is_valid():
                            mun.chairman = man.save()
                    elif data['submit'] == 'd_chair':
                        man = Person2Form(data, instance=mun.deputy_chairman)
                        if man.is_valid():
                            mun.deputy_chairman = man.save()
                    elif data['submit'] == 'admin':
                        man = Person2Form(data, instance=mun.administrator)
                        if man.is_valid():
                            mun.administrator = man.save()
                    else:
                        message = "Errors: " + str(man.errors)
                    
                    mun.save()
                    message="SAVED !"
                    

    if mun.chairman:
        chair = Person2Form(instance=mun.chairman)
    else:
        chair = Person2Form()
    if mun.deputy_chairman:
        d_chair = Person2Form(instance = mun.deputy_chairman)
    else:
        d_chair = Person2Form()
    if mun.administrator:
        admin = Person2Form(instance = mun.administrator)
    else:
        admin = Person2Form()
    persons = {'chairman': chair, 'administrator': admin,
               'deputy_chairman': d_chair}
    return render(request, 'users/landing_lb.html', context={'nodata': True, 'persons': persons, "message": message, 'covid_form': covid_form})

import json
from django.conf import settings

@login_required(login_url="users:login")
def test(request):    
    data = []
    
    if request.GET.get('generate'):
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
            async_task ('covid_gandaki.form.report_generate.generate_mun_list')
            generate_mun_list()
        else:
            generate_mun_list()

        
    context = {}
    return render(request, 'd3js/data.html', context=context)


@login_required(login_url="users:login")
def datatable(request):
    return render(request, 'dtables/drf_datatable.html' )


def make_person(request, values):
    theerrors = []
    person = Person(
        full_name=values['person_name'],
        mobile=values['mobile'],
        location=str("%s,%s" % (values['long'], values['lat'])),
        permanent_address=values['perm_address'],
        current_address=values['temp_address'],
        age=values['age'],
        belong_to_form=3,
        )
    try:
        n = person.save()
    except:
        theerrors.append(
            'Error Saving Person' + values['person_name'] + ' \n The person already exists')

    for x in values['food'].split('\r\n'):
        food = x.split(':')
        if (food[0] == ""):
            continue
        else:
            food = Food(name=food[0], qty=food[1], qty_unit=food[2],
                        sufficiency=food[3], ordered_by=person.id, order_type=1)
            # food.save()
            try:
                food.save()
            except:
                theerrors.append('Error saving food')

    for x in values['members'].split('\r\n'):
        member = x .split(':')
        if (member[0] == ""):
            continue
        else:
            new_member = Person(
                full_name=member[0], age=member[1], belong_to_form=3)
            # new_member.save()
            # fm = Family(head=person, member=new_member)
            try:
                new_member.save()
                fm = Family(head=person, member=new_member)
            except:
                theerrors.append('Error saving ' + member[0])
                pass

    for x in values['medicine'].split('\r\n'):
        medicine = x .split(':')
        if (medicine[0] == ""):
            continue
        else:
            new_medicine = Medicine(name=medicine[0], type_medicine=medicine[1], qty=medicine[2], sufficiency = medicine[3], ordered_by = person.id, order_type=1)
            # new_medicine.save()
        try:
            new_medicine.save()

        except:
            theerrors.append('Error saving ' + medicine[0])

    y = Delivery(person=person, mode_delivery=values['delivery'])
    y.save()

    if len(theerrors) == 0:
        return render(request, 'base/body.html', context={'message': "तपाईले माग गर्नु भएको विवरण तपाईले आफ्नो स्थानीय तह वा वडा बाट लिन सम्पर्क गर्नु होला । हामी सकेसम्म उक्त वस्तुहरु तपाईको नजिकैको स्थानीय तह वा वडामा पठाउने छौ । विवरण माग गर्नु भएकोमा धन्यवाद । भन्ने म्यासेज आउने बनाउनु होला ।"})
    else:
        return render(request, 'form/index.html', context={'errors': theerrors})
    for x in values:
        print(values[x])
    return HttpResponse(values)


def submit_general(request):
    mydict = {
        'person_name':'full_name',
        'mobile':'mobile',
        'perm_address':'permanent_address',
        'age':'age'

    }
    
    values = request.POST
    try:
        make_call = Person.objects.get(mobile=values['mobile'], belong_to_form=3)
        return render(request, 'base/body.html', context={'message': "Submission Already Registered!  \n However it was already entered. Please contact us for making changes. \n It was registered by name " + make_call.full_name})
    except:
        return make_person(request,values)
        


@csrf_exempt
def mun_list(request):
    if request.method == 'GET':
        snippets = Office.objects.all()
        serializer = lb.OfficeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    
