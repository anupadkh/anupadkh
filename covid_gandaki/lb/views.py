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
    context = {'user':request.user}
    return render(request, 'base/data_tables.html', context=context)


@login_required(login_url='users:login')
def list_dtable(request,id):
    mydict = {
        1: ''
    }
    return render(request, 'base/data_tables.html', context=context)
