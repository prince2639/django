from django.apps import AppConfig
from django.shortcuts import render
from .models import Items

class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'

def index(request):
    items = Items.objects.all()
    # print("items:::", items)
    return render(request, 'demo/index_demo.html', {'items': items})
