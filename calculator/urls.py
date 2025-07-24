from django.urls import path
from . import views



urlpatterns = [
    path('',views.calcIndex,name='calc-index')
]