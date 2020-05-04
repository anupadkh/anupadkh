from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from .utils import Table, table_descriptions
import json
from pprint import pprint
@login_required(login_url="admin:login")
@user_passes_test(lambda u: u.is_superuser, login_url="admin:login")
def index(request):
    for x in range(len(table_descriptions)):
        # table_descriptions[x].columns = str(json.dumps(
        #     table_descriptions[x].columns))
        pprint(table_descriptions[x].columns)
    context = {
        'table_descriptions': table_descriptions
    }
    return render(request, 'admin_data/counters.html', context=context)
