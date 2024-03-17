from django.shortcuts import render
from django.http import HttpResponse
from .models import place
# Create your views here.

def demo(request):
    obj =place.objects.all()
    return render(request,"index.html",{'result' : obj})

