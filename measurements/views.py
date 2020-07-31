from django.shortcuts import render
from measurements.models import Area

# Create your views here.
from django.http import HttpResponse


def index(request):
    allAreas = Area.objects.all()
    context = {
        'allAreas': allAreas
    }
    return render(request, 'measurements/index.html', context)