from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

