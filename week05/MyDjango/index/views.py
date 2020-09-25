from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render


def index(request):
    # return HttpResponse('this is an index page !')
    return render(request, 'index.html')