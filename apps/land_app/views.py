# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'land_app/index.html')

#id = (?P<id>)
def show(request, num):
    num = int(num)
    if num >= 1 and num <= 10:
        return render(request, 'land_app/snow.html')
    elif num >= 11 and num <= 20:
        return render(request, 'land_app/desert.html')
    elif num >= 21 and num <= 30:
        return render(request, 'land_app/forest.html')
    elif num >= 31 and num <= 40:
        return render(request, 'land_app/vineyard.html')
    elif num >= 41 and num <=50:
        return render(request, 'land_app/tropical.html')
    else:
        return render(request, 'land_app/error.html')
