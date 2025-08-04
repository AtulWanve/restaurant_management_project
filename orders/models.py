from django.db import models

class Order(models.Model):
    """
    represents a customer's order.
    stores total amount, payment status, and any notes from the customer.
    """
    customer_name = models.CharField(
        max_length=100,
        verbose_name='Customer Name',
        help_text='Name of the person who placed order'
        )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Customer Note',
        help_text='Special instructions or notes from the customer'
         )
    total_order_amount = models.FloatField(
        verbose_name='Total Order Amount',
        help_text='Final total amount of the order'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status',
        help_text='Whether the order is paid or not'
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At',
        help_text='Timestamp when the order was placed'
        )

    def __str__(self):
        return f'Order #{self.pk} by {self.customer_name}'

class OrderItem(models.Model):
    """
    represents an item in an order
    each item is linked to a specific order using a foreign key
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
        null=True,
        verbose_name='Order',
        help_text='The order this item is associated with'
        )
    item_name = models.CharField(
        max_length=100,
        verbose_name='Item Name',
        help_text='Name of the menu item'
        )
    item_price = models.FloatField(
        verbose_name='Item Price',
        help_text='Price per unit of the item'        
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
        help_text='Number of units of this item in the order'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Item Created At',
        help_text='Timestamp when this item was added to the order')

    def __str__(self):
        return f'{self.quantity} x {self.item_name} (Order #{self.order.id})'