from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.add_record, name='add_record'),
    path('<int:pk>/', views.record_detail, name='record_detail'),
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
]