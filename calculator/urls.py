from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.calcIndex,name='calc-index')
]

from calculator.views2 import(
    CalculatorView,
    #extract crud views
    CalculatorCreateView,
    CalculatorDeleteView,
    CalculatorUpdateView,
    CalculatorReadView
    ) 

urlpatterns += [
    path("new/",include(
        [
            path("test/",CalculatorView.as_view()),
            path("",CalculatorReadView.as_view(),name='calc-list'),
            path("create/",CalculatorCreateView.as_view(),name='calc-create'),
            path("delete/<str:pk>/",CalculatorDeleteView.as_view(),name='calc-delete'),
            path("update/<str:pk>/",CalculatorUpdateView.as_view(),name='calc-update')
            
            
        ]
    ))
]