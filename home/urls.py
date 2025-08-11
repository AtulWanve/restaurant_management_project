from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('contact-us', views.contact_us, name='contact-us'),
]
