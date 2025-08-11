from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: This file has both:
1. ItemView - for working with the database and serializer
2. MenuItemView - for a simple hardcoded menu list
'''

# View using database + serializer
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view with hardcoded menu items
class MenuItemView(APIView):
    def get(self, request):
        # hardcoded items for now
        items = [
            {"name": "Pizza", "price": 8.99, "description": "Classic pizza with tomato and cheese"},
            {"name": "Burger", "price": 6.49, "description": "Grilled veggie patty with lettuce and tomato"},
            {"name": "Pasta", "price": 7.99, "description": "Creamy Alfredo sauce with fettuccine"},
        ]
        return Response(items, status=status.HTTP_200_OK)
