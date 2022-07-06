from django.shortcuts import render

from django.http import HttpResponse


def ListQue(request):
    return render(request,'ListProblem.html')

