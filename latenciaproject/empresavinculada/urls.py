from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresasvinculadas_view, name='empresasvinculadas_view'),
    path('<int:id>', views.empresasvinculadas_view, name='empresasvinculadas_view'),
]