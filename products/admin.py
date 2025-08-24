from django.contrib import admin
from .models import Item

# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_fields = ['item_name']
    list_filter = ['created_at']

# Register your models here.
admin.site.register(Item, ItemAdmin)