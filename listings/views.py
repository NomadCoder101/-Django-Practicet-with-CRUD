from django.shortcuts import render,redirect

# Create your views here.
from .models import *

from .forms import CreateForm

def Listings(request):
    
    listings = Listing.objects.all()
    
    context = {'listings':listings}
    
    return render(request, 'listings.html', context)

def SingleListing(request,pk):
    
    listing = Listing.objects.get(id = pk)
    
    context = {'listing':listing}
    
    return render(request, 'single-listings.html', context)
    


def createListing(request):
    
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
        
    context ={
        'form':form
        }
    return render(request,'create.html', context)
    
    
def UpdateListing(request,pk):
    
    listing = Listing.objects.get(id = pk)
    
    form = CreateForm(instance=listing)
    if request.method == 'POST':
        form = CreateForm(request.POST,instance=listing,files=request.FILES)
        print(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
        
    context ={
        'form':form
        }
    return render(request,'update.html', context)


def listingDelete(request,pk):
    listing = Listing.objects.get(id = pk)
    listing.delete()
    return redirect('/')
    