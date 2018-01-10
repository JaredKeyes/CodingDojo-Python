# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for form for new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder for blog {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder for blog {} edit".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')

# Create your views here.
