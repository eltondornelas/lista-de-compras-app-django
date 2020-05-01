from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaIndex.as_view(), name='index'),
]
