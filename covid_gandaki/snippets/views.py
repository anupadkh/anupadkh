from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from covid_gandaki.snippets.modal_serializers.form import *
from covid_gandaki.snippets.modal_serializers import lb, food_meds, public as pc,form, users
from covid_gandaki.snippets.models import Snippet
from covid_gandaki.snippets.serializer import SnippetSerializer

def petrol_list(request):
    if request.method == 'GET':
        snippets = food_meds.Petroleum.objects.all()
        serializer = food_meds.Lb_Petroleum_Serializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    

def sell_list(request):
    if request.method == 'GET':
        snippets = food_meds.Production.objects.all()
        serializer = food_meds.Lb_Production_Serializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    

def need_list(request):
    if request.method == 'GET':
        snippets = pc.Needy.objects.all()
        serializer = pc.NeedySerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
  

def medical_list(request):
    if request.method == 'GET':
        snippets = food_meds.Medical.objects.all()
        serializer = food_meds.Lb_Medical_Serializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    


def hospital_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = lb.Hospital.objects.all()
        serializer = lb.HospitalSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


def relief_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = lb.ReliefFund.objects.all()
        serializer = lb.ReliefFundSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)



def covid_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = pc.QTPerson.objects.all()
        serializer = pc.QTPersonSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)



def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Travel.objects.all()
        serializer = Lb_Travel_Serializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
