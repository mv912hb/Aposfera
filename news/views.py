from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Aposfera')

def test_page(request):
    return HttpResponse('<b><h1><center>Test Page</center></h1></b>')

