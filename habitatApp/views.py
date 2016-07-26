"""Django views - front end logic"""
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Donor, Donation


def index(request):
    """Default HttpResponse"""
    #return HttpResponse("Hello World!")
    donations = Donation.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'habitatApp/index.html', {'donations': donations})

'''
def add_donation(request):
    """Do later"""
    return render(request, 'habitatApp/index.html')
'''