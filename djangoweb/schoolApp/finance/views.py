from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feeCollection(request):
    return HttpResponse("<h1>This is fee collection view</h1>")

def feeDueReport(request):
    return HttpResponse("<h2>This is about fee due report</h2>")

def feeCollectionReport(request):
    return HttpResponse("<h3>This is about fee Collection report</h3>")
