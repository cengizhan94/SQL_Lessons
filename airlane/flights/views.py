from django.shortcuts import render
from . import Flight
# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })
        
