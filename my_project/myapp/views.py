from django.shortcuts import render, HttpResponse
from myapp.models import Item

def index(request):
    # items = Item.objects.all()
    # return HttpResponse("This is home page")
    return render(request, 'index.html')

def about(request):
    # items = Item.objects.all()
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    # items = Item.objects.all()
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contacts(request):
    # items = Item.objects.all()
    # return HttpResponse("This is contacts page")
    return render(request, 'contact.html')

