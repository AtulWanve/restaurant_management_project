from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
]
