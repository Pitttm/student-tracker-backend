from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def student_list (request):
    return HttpResponse("Students tracker backend working")