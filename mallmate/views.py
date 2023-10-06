from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def tima(request):
    return render(request, "tima.html", {'name': 'Timon'})
