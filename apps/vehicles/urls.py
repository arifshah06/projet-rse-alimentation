from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list_view, name='vehicle_list'),
    path('nouveau/', views.vehicle_form_view, name='vehicle_form'),
    path('<int:pk>/', views.vehicle_detail_view, name='vehicle_detail'),
    path('<int:pk>/supprimer/', views.vehicle_delete_view, name='vehicle_delete'),
]
