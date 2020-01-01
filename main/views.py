from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return JsonResponse({'ret': 1, 'info': 'success'})
