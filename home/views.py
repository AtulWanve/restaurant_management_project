from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

def homepage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME,
        'restaurant_phone': settings.RESTAURANT_PHONE
    }
    return render(request, 'home/index.html', context)

def contact_us(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def reservations(request):
    return render(request, 'home/reservations.html')

class MenuItemsView(APIView):
    def get(self, request):
        menu_items = [
            {'id': 1, 'name': 'Pizza', 'price': 9.99},
            {'id': 2, 'name': 'Burger', 'price': 5.99},
            {'id': 3, 'name': 'Pasta', 'price': 7.49},
        ]
        return Response(menu_items)
