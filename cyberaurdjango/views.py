from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

def home(request):
    return render(request, 'index.html')

