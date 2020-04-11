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
from pprint import pprint
from covid_gandaki.snippets.modal_serializers import lb

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

    if request.method=="POST":
        data = request.POST
        man = Person2Form(data)
        with transaction.atomic():
            if man.is_valid():
                instance = man.save(commit=False)
                if data['submit'] == 'chair':
                    if mun.chairman:
                        instance.pk = mun.chairman.pk
                    instance.save()
                    mun.chairman = instance
                elif data['submit'] == 'd_chair':
                    if mun.deputy_chairman:
                        instance.pk = mun.deputy_chairman.pk
                    instance.save()
                    mun.deputy_chairman = instance
                elif data['submit'] == 'admin':
                    if mun.administrator:
                        instance.pk = mun.administrator.pk
                    instance.save()
                    mun.administrator = instance
                else:
                    pass
                mun.save()
                message="SAVED !"
            else:
                message = "Errors: " + str(man.errors)

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
    return render(request, 'users/landing_lb.html', context={'nodata': True, 'persons': persons, "message": message})

def test(request):
    pass


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
    
    
