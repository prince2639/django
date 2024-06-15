from django.shortcuts import render
from .models import Item

# Create your views here.

def Item(request):
    items = Item.objects.all()
    return render(request, 'demo/index_demo.html', {'items': items})
