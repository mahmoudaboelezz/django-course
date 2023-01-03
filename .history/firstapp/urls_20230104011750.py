from django.urls import path 
from .views import index,calculate
urlpatterns = [
    path('index',index),
    path('calculate',calculate)
]
