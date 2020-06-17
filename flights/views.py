from django.shortcuts import render
from flights.models import Flight, Passanger
from django import forms
# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights": Flight.objects.all()
    })

def flights(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)

    except:
        return render(request, 'flights/notfound.html')

    if request.method=='POST':
        id = int(request.POST["passangers"])
        passanger=Passanger.objects.get(id=id)
        passanger.booking.add(flight)


    return render(request,'flights/flight.html',
                  { "flight": flight,
                    "passanger": flight.passanger.all(),
                     "non_passangers": Passanger.objects.exclude(booking=flight).all(),
                    })

