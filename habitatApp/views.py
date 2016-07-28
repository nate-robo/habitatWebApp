"""Django views - front end logic"""
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .models import Donor, Donation
from .forms import DonationForm


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
            return redirect('donation_detail', pk=post.pk)
    else:
        form = DonationForm(instance=donation)
    return render(request, 'habitatApp/donation_edit.html', {'form': form})



'''
def add_donation(request):
    """Do later"""
    return render(request, 'habitatApp/index.html')
'''
