from django.db import models
from django.contrib.auth.models import User
from products.models import Item

class Order(models.Model):
    """
    represents a customer's order.
    stores total amount, payment status, and any notes from the customer.
    """
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Customer',
        help_text='User who placed this order'
        )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Customer Note',
        help_text='Special instructions or notes from the customer'
         )
    total_order_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
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
        return f'Order #{self.pk} by {self.customer.username}'

class OrderItem(models.Model):
    """
    represents an item in an order
    each item is linked to a specific order using a foreign key
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        null=True,
        verbose_name='Order',
        help_text='The order this item is associated with'
        )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Menu Item',
        help_text='Name of the menu item'
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
        return f'{self.quantity} x {self.item.item_name} (Order #{self.order.id})'

    @property
    def total_price(self):
        """
        returns the total price for this item (price * quantity).
        """
        return self.quantity * self.item.item_price