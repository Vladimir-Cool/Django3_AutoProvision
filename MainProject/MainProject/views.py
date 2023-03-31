from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'MainProject/index.html')

def content(request):
    return render(request, 'MainProject/content.html')

