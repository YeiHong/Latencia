from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.avanzo_view, name='avanzo_view'),
    path('<int:pk>', views.avanzo_view, name='avanzo_)view')
]