from django.urls import path
from other import views

app_name = 'other'
urlpatterns = [
    path('user-contact/', views.userContact, name='user-contact'),
    path('faq-view/', views.faq_view, name='faq-view'),
    path('about-eshop/', views.about_eshop, name='about-eshop'),
]