from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .core import expenses_by_category


def home(request):
    return render(request, 'homepage.html')

def chart_data(request):
    data = expenses_by_category()
    return JsonResponse(data)
