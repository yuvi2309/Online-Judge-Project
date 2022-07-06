from django.urls import path
from .import views

urlpatterns = [
    path('ListProblem/',views.ListQue)
]
