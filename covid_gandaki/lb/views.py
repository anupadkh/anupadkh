from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from .models import *

def index(request):
    context = {}
    return render(request, 'lb/need_assessment.html', context=context)

def submit(request):
    return "Hello"

def lbody(request):
    context={'user':request.user}


@login_required(login_url='users:login')
def index_dtable(request):
    context = {'user':request.user, 'login':True}
    return render(request, 'base/data_tables.html', context=context)


@login_required(login_url='users:login')
def list_dtable(request,id):
    headings = [
        'विदेशवाट मा आएकाहरुको विवरण',
        'क्वारेन्टाईन र आईसोलेसन सम्वन्धि विवरण',
        'COVID 19 टेस्ट सम्वन्धि विवरण',
        'स्थानियतहलाई आवश्यक पर्ने खाद्यवस्तु  र पशुपंक्षिको दाना, ग्याँस, पेट्रोलियम पदार्थ',
        'स्थानियतहमा उत्पादित तर बिक्रि हुन नसकी खेर गईरहेको वस्तुः',
        'तत्काल आवश्यक औषधि र मेडीकल उपकरण (PPE, मास्क, सेनिटाईजर, साबुन, थर्मोमिटर, पन्जा आदि) सम्वन्धि विवरण',
        'सडक वालवालिका र दैनिक ज्यालामा काम गर्ने कामदार, क्वारेन्टाइनमा बसेका र आर्थिक रुपमा आफै किनेर खाने क्षमता नभएका (Needy People) सम्वन्धि विवरण'
        ]
    mydict = {
        0: 'base/data_tables.html',
        1: 'data/isolation.html',
        2: 'data/covid_cases.html',
        3: 'data/petroleum.html',
        4: 'data/production.html',
        5: 'data/medical.html',
        6: 'data/need.html',
    }
    context = {'login': True, "heading":headings[id]}
    if id==1:
        # context = {'login': True,'table2_set':True}
        context['table2_set'] = True
    
    return render(request, mydict[id], context=context)
