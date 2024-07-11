from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.models import User
import json

def home(request):
    if request.user.is_authenticated:
        return HttpResponse('Вы зарегестрированны')
    else:
        return render(request, 'home.html')

def reg(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
