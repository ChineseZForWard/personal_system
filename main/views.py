from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'main/index.html', context)
