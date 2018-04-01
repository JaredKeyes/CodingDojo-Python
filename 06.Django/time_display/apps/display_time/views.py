# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, HttpResponse

def index(request):
    now =datetime.now().strftime("%H:%M %p, %B %d, %Y")
    context = {
        'i': now
    }
    return render(request,'display_time/index.html', context)


# Create your views here.
