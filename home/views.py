from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def homepage(request):
    try:
        context = {
            'restaurant_name': settings.RESTAURANT_NAME,
            'restaurant_phone': settings.RESTAURANT_PHONE
        }
        return render(request, 'home/index.html', context)
    except Exception as e:
        logger.error(f'Error loading homepage: {e}')
        return render(request, 'home/index.html', {
            'restaurant_name': 'Unknown',
            'restaurant_phone': 'Unavailable'
        })

def contact_us(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def reservations(request):
    return render(request, 'home/reservations.html')

class MenuItemsView(APIView):
    def get(self, request):
        try:
            menu_items = [
                {'id': 1, 'name': 'Pizza', 'price': 9.99},
                {'id': 2, 'name': 'Burger', 'price': 5.99},
                {'id': 3, 'name': 'Pasta', 'price': 7.49},
            ]
            return Response(menu_items)
        except Exception as e:
            # log the error for debugging
            logger.error(f'Error fetching menu items: {e}')
            return Response(
                {'error': 'Unable to load menu items at the moment.'},
                status=500
            )
