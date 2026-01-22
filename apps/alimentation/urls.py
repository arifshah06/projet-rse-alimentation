# apps/alimentation/urls.py
from django.urls import path
from . import views

app_name = "alimentation"

urlpatterns = [
    path("", views.foodentry_list, name="list"),
    path("nouvelle/", views.foodentry_create, name="create"),
]
