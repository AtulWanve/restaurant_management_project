from django.urls import path
from .views import ItemView, MenuItemView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/', MenuItemView.as_view(), name='menu-items'),
]