from django.db import models

class Order(models.Model):
    # stores overall details of an order
    customer_name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    total_order_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} by {self.customer_name}'

class OrderItem(models.Model):
    # stores individual items in an order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    qnty = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.qnty} x {self.item_name} (Order #{self.order.id})'