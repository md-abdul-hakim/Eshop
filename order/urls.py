from django.urls import path
from order import views

app_name = 'order'
urlpatterns = [
    path('add-to-wish/<int:pk>/', views.add_to_wish, name='add-to-wish'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('wish-view/', views.wish_view, name='wish'),
    path('cart-view/', views.cart_view, name='cart'),
    path('track/', views.tracker, name='track'),
    path('remove-item/<int:pk>/', views.remove_item_from_cart, name='remove-item'),
    path('remove-wish/<int:pk>/', views.remove_item_from_wish, name='remove-wish'),
    path('increase-quantity/<int:pk>/', views.increase_cart, name='increase'),
    path('decrease-quantity/<int:pk>/', views.decrease_cart, name='decrease'),
]