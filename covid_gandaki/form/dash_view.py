from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
from covid_gandaki.snippets.modal_serializers import lb

# Create your views here.
# @login_required(login_url='users:login')

from django.db import transaction

@staff_member_required(login_url="admin:login")
def create_dashboard(request,id=None):
    if id==None:
        id=2
    applications = {
        0: {
            'app': 'form',
            'model': 'Travel',
            'heading': 'विदेशवाट ' + request.session['employee'] + 'मा आएकाहरुको विवरण',
            'page': 'jdata/travel.html',
            'url': '/router/travel/',
        },
        1: {
            'app': 'lb',
            'model': 'Hospital',
            'heading': 'क्वारेन्टाईन र आईसोलेसन सम्वन्धि विवरण',
            'page': 'jdata/quarantine.html',
            'url': '/snip/hospitals/',
        },
        2: {
            'app': 'public',
            'model': 'QTPerson',
            'heading': 'COVID 19 टेस्ट सम्वन्धि विवरण',
            'page': 'jdata/dashboard/index.html',
            'url': '/router/covid/',
        },
        3: {
            'app': 'food_meds',
            'model': 'Petroleum',
            'page': 'jdata/petroleum.html',
            'heading': 'स्थानियतहलाई आवश्यक पर्ने खाद्यवस्तु  र पशुपंक्षिको दाना, ग्याँस, पेट्रोलियम पदार्थ',
            'url': '/router/supplies/',

        },
        4: {
            'app': 'food_meds',
            'model': 'Production',
            'page': 'jdata/production.html',
            'heading': 'स्थानियतहमा उत्पादित तर बिक्रि हुन नसकी खेर गईरहेको वस्तुः',
            'url': '/router/sell/',
        },
        5: {'page': 'jdata/medical.html',
            'app': 'food_meds',
            'model': 'Medical',
            'heading': 'तत्काल आवश्यक औषधि र मेडीकल उपकरण (PPE, मास्क, सेनिटाईजर, साबुन, थर्मोमिटर, पन्जा आदि) सम्वन्धि विवरण',
            'url': '/router/medical/',
            },
        6: {
            'page': 'jdata/needy.html',
            'app': 'public',
            'model': 'Needy',
            'heading': 'सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण',
            'url': '/router/needy/',
        },
        7: {
            # 'app': 'lb',
            # 'model': 'sub_models.rahat.'
            'heading': 'राहत सम्बन्धी जानकारी',
            'url': '/router/relief/',
            'page': 'jdata/relief.html'
        },
    }

    if id < 1:
        # App = apps.get_model(app_label=applications[id]['app'], model_name=applications[id]['model'])
        context = {
            'login': True, "heading": applications[id]['heading'], 'url': applications[id]['url']}
    elif id < 7:
        context = {
            'login': True, "heading": applications[id]['heading'], 'url': applications[id]['url'], 'next_page': id+1}
    elif id == 7:
        # App = ReliefFund.objects.filter
        context = {
            'login': True, "heading": applications[id]['heading'], 'url': applications[id]['url']}
    else:
        return redirect('lb:table_view', id=0)
    return render(request, 'jdata/dashboard/index.html', context=context)
