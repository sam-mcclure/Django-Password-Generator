from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_-+=[]{}?<>;:')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 12))
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

