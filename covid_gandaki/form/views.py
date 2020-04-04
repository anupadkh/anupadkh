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
from pprint import pprint
from covid_gandaki.snippets.modal_serializers import lb

# Create your views here.
# @login_required(login_url='users:login')

from django.db import transaction

def index(request):
    # return render(request, 'polls/detail.html', {'question': question})
    return render(request, 'form/index.html', context={})
    return HttpResponse('Hello')

def test(request):
    return render(request,'dtables/data_good.html')

@transaction.atomic
def submit_general(request):
    mydict = {
        'person_name':'full_name',
        'mobile':'mobile',
        'perm_address':'permanent_address',
        'age':'age'

    }
    theerrors = []
    values = request.POST
    try:
        make_call = Person.objects.get(mobile=values['mobile'])

        return render(request, 'base/body.html', context={'message': "Submission Already Registered!  However it was already entered. Please contact us for making changes."})
    except:
        person = Person(
            full_name=values['person_name'],
            mobile=values['mobile'],
            location=str("%s,%s"%(values['long'], values['lat'])),
            permanent_address = values['perm_address'],
            current_address = values['temp_address'],
            age = values['age']
            )
        try:
            n = person.save()
        except:
            theerrors.append('Error Saving Person')

        for x in values['food'].split('\r\n'):
            food = x.split(':')
            if (food[0] == ""):
                continue
            else:
                food = Food(name=food[0], qty=food[1], qty_unit=food[2], sufficiency=food[3], ordered_by=person.id, order_type=1)
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
                new_member = Person(full_name=member[0], age=member[1])
                # new_member.save()
                # fm = Family(head=person, member=new_member)
                try:
                    new_member.save()
                    fm = Family(head=person, member=new_member)
                except:
                    theerrors.append('Error saving '+ member[0])
                    pass

        for x in values['medicine'].split('\r\n'):
            medicine = x .split(':')
            if (medicine[0] == ""):
                continue
            else:
                new_medicine = Medicine(name=medicine[0], type_medicine=medicine[1], qty= medicine[2], sufficiency = medicine[3], ordered_by = person.id, order_type=1)
                # new_medicine.save()
            try:
                new_medicine.save()

            except:
                theerrors.append('Error saving '+ medicine[0])

        
        y = Delivery(person=person, mode_delivery=values['delivery'])
        y.save()
            
        if len(theerrors) == 0:
            return render(request, 'base/body.html', context={'message': "Submit Successful! तपाईँको माग दर्ता भएको छ ।  हामी तपाईँलाई मोबाइलमा सम्पर्क गर्नेछौँ । धन्यवाद "})
        else:
            return render(request, 'form/index.html', context={'errors' : theerrors})
    for x in values:
        print(values[x])
    return HttpResponse(values)


@csrf_exempt
def mun_list(request):
    if request.method == 'GET':
        snippets = Office.objects.all()
        serializer = lb.OfficeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    

food_package = [
    {"सामानको विवरण": "चामल स्टिम जिरा (राम्रो)", "परिमाण": "२५ के.जि.",
     "दर": "६६।–", "जम्मा मूल्य": "१६५०।–"},
    {"सामानको विवरण": "पिठो (आँटा) चक्की", "परिमाण": "५ के.जि.",
     "दर": "६०।–", "जम्मा मूल्य": "३००।–"},
    {"सामानको विवरण": "दाल (रहर, मास, मुसुरो)", "परिमाण": "२ के.जि.",
     "दर": "१३०।–", "जम्मा मूल्य": "२६०।–"},
    {"सामानको विवरण": "चीनी", "परिमाण": "१ के.जि.",
        "दर": "८०।–", "जम्मा मूल्य": "८०।–"},
    {"सामानको विवरण": "सनफ्लावर तेल", "परिमाण": "२ लिटर",
        "दर": "१६०।–", "जम्मा मूल्य": "३२०।–"},
    {"सामानको विवरण": "सेतो केराउ", "परिमाण": "२ के.जि.",
        "दर": "७५।–", "जम्मा मूल्य": "१५०।–"},
    {"सामानको विवरण": "आयो नुन", "परिमाण": "२ के.जि.",
        "दर": "२०।–", "जम्मा मूल्य": "४०।–"},
    {"सामानको विवरण": "चिउरा", "परिमाण": "२ के.जि.",
        "दर": "८०।–", "जम्मा मूल्य": "१६०।–"},
    {"सामानको विवरण": "चियापत्ती", "परिमाण": "५०० ग्राम",
        "दर": "२००।–", "जम्मा मूल्य": "२००।–"},
    {"सामानको विवरण": "मसला", "परिमाण": "२०० ग्राम",
        "दर": "१००।–", "जम्मा मूल्य": "१००।–"},
    {"सामानको विवरण": "वेसार", "परिमाण": "१०० ग्राम",
        "दर": "४०।–", "जम्मा मूल्य": "४०।–"},
    {"सामानको विवरण": "चाउचाउ", "परिमाण": "५ प्याकेट",
        "दर": "१६।–", "जम्मा मूल्य": "८०।–"},
    {"सामानको विवरण": "चना", "परिमाण": "१ के.जि.",
        "दर": "१२०।–", "जम्मा मूल्य": "१२०।–"}
]
