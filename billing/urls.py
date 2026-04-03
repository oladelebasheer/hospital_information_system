from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('add/', views.add_bill, name='add_bill'),
    path('payment/add/', views.add_payment, name='add_payment'),
]