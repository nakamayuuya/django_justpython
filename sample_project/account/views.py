from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse(200)

url = reverse('account:index')