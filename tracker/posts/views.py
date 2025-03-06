from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from tracker.core import expenses_by_category
from django.http import JsonResponse



# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'posts/book_list.html', {'books': books})

def book_page(request, slug):
    return HttpResponse(slug)

def chart_data(request):
    data = expenses_by_category()
    return JsonResponse(data)

