from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
import uuid
from django.utils import timezone

class PlaceOrderView(APIView):
    # API view to handle placing a new order with multiple items

    def post(self, request):
        data = request.data
        items = data.get('items', [])

        # validate items list
        if not items:
            return Response({'error': 'Items list cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        # validate and compute total
        total_amount = 0
        for item in items:
            try:
                price = float(item['item_price'])
                quantity = int(item['quantity'])
                if price < 0 or quantity <= 0:
                    return Response({'error':'Invalid price or quantity in item'}, status=status.HTTP_400_BAD_REQUEST)
                total_amount += price * quantity
            except (KeyError, ValueError):
                return Response({'error': 'Each item must have item_price (float) and quantity (int)'}, status=400)

        # create order
        order = Order.objects.create(
            order_id = uuid.uuid4(),
            customer_name=data.get('customer_name', ''),
            note=data.get('note', ''),
            is_paid=data.get('is_paid', False),
            total_order_amount=total_amount,
            created_at=timezone.now()
        )

        # create orderitems
        for item in items:
            OrderItem.objects.create(
                order=order,
                item_name=item['item_name'],
                item_price=float(item['item_price']),
                quantity=item['quantity'],
                created_at=timezone.now()
            )

        # build response
        response_data = {
            'order_id': str(order.order_id),
            'customer_name': order.customer_name,
            'note': order.note,
            'is_paid': order.is_paid,
            'total_order_amount': order.total_order_amount,
            'created_at': order.created_at.isoformat(),
            'items': items
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

