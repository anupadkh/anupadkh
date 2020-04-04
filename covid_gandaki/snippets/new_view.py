from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from covid_gandaki.users.models import Employee
from covid_gandaki.snippets.modal_serializers.form import *
from covid_gandaki.snippets.modal_serializers import lb, food_meds, public as pc,form, users
from covid_gandaki.snippets.models import Snippet
# from covid_gandaki.snippets.serializer import SnippetSerializer
from django.db import transaction

@csrf_exempt
def relief_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = lb.ReliefFund.objects.all()
        serializer = lb.ReliefFundSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = lb.ReliefFundSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@transaction.atomic
def user(request):
    if request.method =='POST':
        data = request.POST
        serializer = users.CreateUserSerializer(data=data)
        if serializer.is_valid():
            user_instance = serializer.save()
            mun = lb.Office.objects.get(id=data['municipality'])
            emp = Employee(user = user_instance, municipality = mun)
            emp.save()
            request.session['message'] = "You have been registered. Please contact MOITFE to activate."
            return redirect('users:login')
        request.session['message'] = "You couldn't be registered. Error with " + str(serializer.errors)
        return redirect('users:login')
    
    return redirect('users:login')
    
    # if request.method = 'GET':



# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
