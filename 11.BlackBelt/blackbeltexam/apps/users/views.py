# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, Trip, Trip_Join
from datetime import datetime

# Create your views here.
def home(request):
    return redirect('/users/new')

def new(request):
    return render(request, '/users/new.html')

def create(request):
    if request.method == 'POST':
        result = User.objects.validate_registration(request.POST)
        if result['status'] == False:
            for error in result['errors']:
                messages.error(request, error)
            return redirect('/users/new')
        else:
            request.session['user_id'] = result['user'].id
            return redirect('/users/success')

def success(request):
    return render(request, 'users/home.html')

def authenticate(request):
    if request.method == 'POST':
        result = User.objects.validate_login(request.POST)
        if result['status'] == False:
            messages.error(request, result['error'])
            return redirect('/users/new')
        else:
            request.session['user_id'] = result['user'].id
            return redirect('/users/success')

def logout(request):
    request.session.flush
    return redirect('/users/new')

def current_User(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

def home(request):
    availableTrips = []

    user = User.objects.get(id=request.session['user_id'])
    availableTrips = Trip.objects.order_by('start_date')

    context = {

        'user' : user,
        'trips' : Trip.objects.filter(user=user),
        'attending' : Trip_Join.objects.filter(attendee=user),
        'othersTrips' : availableTrips
    }
    return render(request, '/users/new.html', context)

def join(request, id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    Trip_Join.objects.create(trip=trip, attendee=user)

    messages.add_message(request, messages.INFO, 'You are joining trip ' + str(id))
    return redirect(reverse('home'))

def add(request):
    return render(request, '/users/add.html')

def add_travel(request):
    for field in request.POST:
        if len(request.POST[field]) < 1:
            messages.add_message(request, messages.INFO, 'All fields are required!')
            return redirect(reverse('add'))
            break
    try:
        startDate = datetime.datetime.strptime(request.POST['start_date'],'%m/%d/%Y')
        endDate = datetime.datetime.strptime(request.POST['end_date'],'%m/%d/%Y')

        if startDate < datetime.datetime.now():
            messages.add_message(request, messages.INFO, 'Start Date must be after today. Must be in MM/DD/YYYY format.')
            return redirect(reverse('add'))
        elif startDate > endDate:
            messages.add_message(request, messages.INFO, 'End Date must be after Start Date. Must be in MM/DD/YYYY format.')
            return redirect(reverse('add'))
    except Exception,e:
        messages.add_message(request, messages.INFO, 'The dates entered are invalid. Must be in MM/DD/YYYY format.')
        return redirect(reverse('add'))


    user = User.objects.get(id=request.session['user_id'])
    Trip.objects.create(user=user, destination=request.POST['destination'], start_date=startDate, end_date=endDate, plan=request.POST['description'])
    return redirect(reverse('home'))

def trip_detail(request, id):
    attendees = None
    try:
        attendees = Trip_Join.objects.filter(trip=id)
    except:
        pass

    context = {
        "trip" : Trip.objects.get(id=id),
        "attendees" : attendees
        }
    return render(request, '/users/trip_detail.html', context)