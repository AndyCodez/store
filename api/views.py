from django.shortcuts import render, HttpResponse
from .models import Customer
# Create your views here.

def index(request):
    customers = Customer.objects.all()
    return HttpResponse(customers)
    