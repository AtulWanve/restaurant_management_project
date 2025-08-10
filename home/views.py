from django.shortcuts import render
from django.conf import settings

def homepage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home/index.html')