from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from decimal import Decimal, InvalidOperation
import uuid
from django.utils.timezone import now

class PlaceOrderView(APIView):
    # API view to handle placing a new order with multiple items

    def post(self, request):
        data = request.data
        items = data.get('items', [])

        # validate items list
        if not items:
            return Response({'error': 'Items list cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        # validate and compute total
        total_amount = Decimal('0.00')
        for item in items:
            try:
                price = Decimal(str(item['item_price']))
                quantity = int(item['quantity'])
                if price < 0 or quantity <= 0:
                    return Response({'error':'Invalid price or quantity in item'}, status=status.HTTP_400_BAD_REQUEST)
                total_amount += price * quantity
            except KeyError as e:
                return Response({'error': f'Missing key: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)
            except (ValueError, InvalidOperation):
                return Response({'error': 'Invalid data types for price or quantity'}, status=status.HTTP_400_BAD_REQUEST)

        # create order
        order = Order.objects.create(
            order_id = uuid.uuid4(),
            customer_name=data.get('customer_name', ''),
            note=data.get('note', ''),
            is_paid=data.get('is_paid', False),
            total_order_amount=total_amount,
            created_at=now()
        )

        # save order items
        for item in items:
            OrderItem.objects.create(
                order=order,
                item_name=item['item_name'],
                item_price=Decimal(str(item['item_price'])),
                quantity=item['quantity'],
                created_at=now()
            )

        # retrieve saved items from DB to avoid mismatches
        order_items = order.items.all()
        
        # build response using actual saved items
        response_data = {
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'note': order.note,
            'is_paid': order.is_paid,
            'total_order_amount': str(order.total_order_amount),
            'created_at': order.created_at.isoformat(),
            'items': [
                {
                    'item_name': oi.item_name,
                    'item_price': str(oi.item_price),
                    'quantity': oi.quantity,
                    'created_at': oi.created_at.isoformat()
                }
                for oi in order_items
            ]
        }

        return Response(response_data, status=status.HTTP_201_CREATED)