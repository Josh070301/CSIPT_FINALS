from django.shortcuts import render, redirect
from .models import sched
from django import forms
from django.views.decorators.csrf import csrf_protect

def schedule(request):
    allSched = sched.objects.all()
    context = {
        'schedules' : allSched.values,
    }
    return render(request, "schedule.html", context)


def make(request):
    allSched = sched.objects.all()
    result = 'Please fill all information'
    if request.method == "POST":
        set_shipId = request.POST.get('shipId')
        set_vessel = request.POST.get('vessel')
        set_origin = request.POST.get('origin')
        set_destination = request.POST.get('destination')
        set_date = request.POST.get('date')
        set_time = request.POST.get('time')
        set_seats = request.POST.get('seats')
        set_vehicles = request.POST.get('vehicles')
        set_price = request.POST.get('price')
        set_status = request.POST.get('status')
        if  not set_shipId or not set_vessel or not set_origin or not set_destination or not set_date or not set_time or not set_seats or not set_vehicles or not set_price or not set_status:
            result = 'Please fill all required information'
            context = {
                'schedules' : allSched.values,
                'result' : result,
            }
            return render(request, "create.html", context)
        else:
            sched.objects.create(shipId = set_shipId, vessel = set_vessel, origin = set_origin, destination = set_destination, date = set_date, time = set_time, seats = set_seats, vehicles = set_vehicles, price = set_price, status = set_status)
            result = 'Schedule added successfully'
            
    context = {
    'schedules' : allSched.values,
    'result' : result,
    }
    return render(request, "create.html", context)

def deleteData(request,pk):
    dele = sched.objects.get(pk = pk)
    dele.delete()
    return redirect('/')

@csrf_protect
def update(request, pk):
    newSched = sched.objects.filter(pk = pk)
    result = 'Please Update the full form'
    if request.method == "POST":
        set_shipId = request.POST.get('shipId')
        set_vessel = request.POST.get('vessel')
        set_origin = request.POST.get('origin')
        set_destination = request.POST.get('destination')
        set_date = request.POST.get('date')
        set_time = request.POST.get('time')
        set_seats = request.POST.get('seats')
        set_vehicles = request.POST.get('vehicles')
        set_price = request.POST.get('price')
        set_status = request.POST.get('status')
        if  not set_shipId or not set_vessel or not set_origin or not set_destination or not set_date or not set_time or not set_seats or not set_vehicles or not set_price or not set_status:
                result = 'Please enter required information to update'
                context = {
                    'update' : newSched.values,
                    'result' : result,
                }
                return render(request, "update.html", context)
        else:
            newSched.update(shipId = set_shipId, vessel = set_vessel, origin = set_origin, destination = set_destination, date = set_date, time = set_time, seats = set_seats, vehicles = set_vehicles, price = set_price, status = set_status)
            result = 'Schedule Update successfully'
            
            
    context = {
        'update' : newSched.values,
        'result' : result,
    }
    return render(request, 'update.html', context)

def search_me(request):
    query = request.GET.get('search')
    result1 = sched.objects.filter(scheduleId__contains = query)
    count = result1.count()
    if result1 is None:
        return render(request, 'search.html', context)
    
    context = {
        'result' : query,
        'search' : result1,
        'total' : count,
    }   
    return render(request, 'search.html', context)