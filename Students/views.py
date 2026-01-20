from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def student_list (requestO):
    return HttpResponse("Students tracker backend working")