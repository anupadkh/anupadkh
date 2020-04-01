from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    context = {}
    return render(request, 'lb/need_assessment.html', context=context)

def submit(request):
    return "Hello"


def index_dtable(request):
    context = {}
    return render(request, 'base/data_tables.html', context=context)
