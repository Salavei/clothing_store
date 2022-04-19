from django.shortcuts import render
from .models import Items


def home(request):
    items = Items.objects.all()
    context = {'items': items}
    return render(request, 'base/home.html', context)


def delivery(request):
    context = {}
    return render(request, 'base/delivery.html', context)


def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)