from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

from django.apps import apps
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
# Create your views here.
from .models import Person2
from covid_gandaki.users.models import Employee
from .forms import Person2Form
from covid_gandaki.lb.sub_models.rahat import ReliefFund, ReliefItem
from covid_gandaki.public.models import Person
from covid_gandaki.food_meds.models import FoodName
from covid_gandaki.snippets.modal_serializers import lb
from django.db import transaction
from django.http import JsonResponse

def index(request):
    context = {}
    return render(request, 'lb/need_assessment.html', context=context)

def submit(request):
    return "Hello"

def lbody(request):
    context={'user':request.user}

import json
@login_required(login_url='users:login')
def reliefs(request, id):
    context = {
        'login': True, 
        "heading": "राहत वितरण भएकाहरुको सुची",
        "url":"/locla",
        "submittor":id
        }
    employee = Employee.objects.get(user=request.user)
    mun = employee.municipality.address.mun

    if request.method == 'GET':
        foods = FoodName.objects.filter(mun=mun)
        context['foods'] = foods
        page = "jdata/relief/lb_distributor.html"
        return render(request, page, context=context)

    elif request.method == 'POST':
        data = request.body
        data = json.loads(data)
        try:
            rf = ReliefFund.objects.get(id=id)
            distributer = rf.submitter
        except:
            return JsonResponse({"message":{"error": "There is no such submitter"}, "status":"false"}, status=500)
        
        # rf, rf2 = ReliefFund.objects.get_or_create(submitter = distributer, office=employee.municipality)
        # if rf2:
        #     rf = rf2
        
        foods = FoodName.objects.filter(mun=mun)
        with transaction.atomic():
            person = lb.ReliefPersonSerializer(data=data , context={'request':request})
            if person.is_valid():
                receiver = person.save()
            else:
                return JsonResponse({'status':'false', 'message':{"errors":{"message":"Please check the input format for the data inserted", "data":data, "errors":person.errors}}}, status=500)
            
            for y in foods:
                obj,created = ReliefItem.objects.get_or_create(receiver = receiver, food_type=y, fund=rf)
                obj.qty = data[str(y.id)]
                # obj.is_valid()
                obj.save()
            
        serializer = lb.ReliefPersonSerializer(receiver)
        return JsonResponse(serializer.data)
            
                


    
    


@login_required(login_url='users:login')
def index_dtable(request):
    # response = requests.get('http://localhost:8000/router/users/')
    # obj = response.json()

    # Dummy data 
    obj = {'name':1,'age':90} 
    context = {'user':request.user, 'login':True, 'object_list':obj}
    return render(request, 'base/data_tables.html', context=context)

# class index_dtable(ListView):
#     model = Person2
#     template_name = 'base/data_tables.html'


@login_required(login_url='users:login')
def list_dtable(request,id):
    applications = {
        0:{
            'app': 'form',
            'model': 'Travel',
            'heading': 'विदेशवाट ' + request.session['employee'] +'मा आएकाहरुको विवरण',
            'page': 'jdata/travel.html',
            'url':'/router/travel/',
        },
        1:{
            'app': 'lb',
            'model': 'Hospital',
            'heading':'क्वारेन्टाईन र आईसोलेसन सम्वन्धि विवरण',
            'page': 'jdata/quarantine.html',
            'url': '/router/quarantines/',
        },
        2:{
            'app': 'public',
            'model': 'QTPerson',
            'heading': 'COVID 19 टेस्ट सम्वन्धि विवरण',
            'page':'jdata/covid.html',
            'url':'/router/covid/',
        },
        3:{
            'app': 'food_meds',
            'model': 'Petroleum',
            'page' : 'jdata/petroleum.html',
            'heading':'स्थानियतहलाई आवश्यक पर्ने खाद्यवस्तु  र पशुपंक्षिको दाना, ग्याँस, पेट्रोलियम पदार्थ',
            'url' : '/router/supplies/',

        },
        4:{
            'app': 'food_meds',
            'model': 'Production',
            'page':'jdata/production.html',
            'heading': 'स्थानियतहमा उत्पादित तर बिक्रि हुन नसकी खेर गईरहेको वस्तुः',
            'url' : '/router/sell/',
        },
        5:{ 'page' : 'jdata/medical.html',
            'app': 'food_meds',
            'model': 'Medical',
            'heading': 'तत्काल आवश्यक औषधि र मेडीकल उपकरण (PPE, मास्क, सेनिटाईजर, साबुन, थर्मोमिटर, पन्जा आदि) सम्वन्धि विवरण',
            'url' : '/router/medical/',
        },
        6:{
            'page':'jdata/needy.html',
            'app': 'public',
            'model': 'Needy',
            'heading': 'सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण',
            'url' : '/router/needy/',
        },
        7:{
            # 'app': 'lb',
            # 'model': 'sub_models.rahat.'
            'heading' : 'राहत सम्बन्धी जानकारी',
            'url' : '/router/relief/',
            'page': 'jdata/relief.html'
        },
    }

    if  id<7:
        # App = apps.get_model(app_label=applications[id]['app'], model_name=applications[id]['model'])
        context = {'login': True, "heading":applications[id]['heading'], 'url':applications[id]['url']}
    elif id == 7:
        # App = ReliefFund.objects.filter
        context = {
            'login': True, "heading": applications[id]['heading'], 'url': applications[id]['url']}
    else:
        return redirect('lb:table_view',id=0)
    return render(request, applications[id]['page'], context=context)


class Person2CreateView(CreateView):
    model = Person2
    form_class = Person2Form
    template_name = 'form/Person2_create.html'
