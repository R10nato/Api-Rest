from django.shortcuts import render
from django.http import HttpResponse


# minhas views
def home(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'form.html')