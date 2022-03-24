from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def landing(request):
    return render(request, "index.html")

def rooms(request):
    return render(request, "room.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contactus.html")

def reserve(request):
    return render(request, "reservation.html")