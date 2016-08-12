"""Django views - front end logic"""
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import Donor, Donation
from .forms import DonationForm, DonorForm
import json



def base(request):
    return render(request, 'habitatApp/base.html')

def donations(request):
    """Default HttpResponse"""
    donors = Donor.objects.all()
    donations = Donation.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'habitatApp/index.html', {'donations': donations, 'donors': donors})


def donation_new(request):
    """Serve client html form for adding donation"""

    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            #Manual form work here
            form.save()
            return redirect('donations')
    else:
        form = DonationForm()
    return render(request, 'habitatApp/donation_new.html', {'form': form})

def donation_detail(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    return render(request, 'habitatApp/donation_detail.html', {'donation': donation})

def donation_edit(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == "POST":
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            donation = form.save(commit=False)
            #Manual form work here
            form.save()
            return redirect('donation_detail', pk=donation.pk)
    else:
        form = DonationForm(instance=donation)
    return render(request, 'habitatApp/donation_edit.html', {'form': form})

def donation_delete(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    donation.delete()
    messages.success(request, 'Donation successfully deleted from database')
    return redirect('donations')

def donors(request):
    donors= Donor.objects.all()
    donations = Donation.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'habitatApp/donors.html', {'donations': donations, 'donors': donors})

def donor_detail(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    donations = Donation.objects.all()
    my_donations = donations.filter(donor=donor)
    return render(request, 'habitatApp/donor_detail.html', {'donor': donor, 'my_donations': my_donations})

def donor_new(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            #Manual work (if needed)
            form.save()
            return redirect('donors')
    else:
        form = DonorForm()
    return render(request, 'habitatApp/donor_new.html', {'form': form})

def donor_edit(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    if request.method == "POST":
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            donation = form.save(commit=False)
            form.save()
            return redirect('donor_detail', pk=donor.pk)
    else:
        form = DonorForm(instance=donor)
    return render(request, 'habitatApp/donor_edit.html', {'form': form})

def donor_delete(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    #donor = Donor.objects.get(pk=int(request.GET['id']))
    donor.delete()
    payload = {'success': True}
    messages.success(request, 'Donor successfully deleted from database')
    return redirect('donors')




'''
def add_donation(request):
    """Do later"""
    return render(request, 'habitatApp/index.html')
'''
