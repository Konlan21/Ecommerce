from itertools import product
from django.shortcuts import render
from django.db.models import Count, Func, F
from store.models import Collection, Product, Customer


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Konlan', 'products': list()})
