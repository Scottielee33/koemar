from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {'name': 'Scottie'}
    return render(request, 'form/home.html', context)