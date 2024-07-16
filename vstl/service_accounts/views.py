from django.shortcuts import render, redirect
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def registration(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        password = data['password']
        username = data['login']
        email = data['email']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "not ok"})
            
def authorization(request):
    if request.method == 'GET':
        return render(request, 'aut.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        username = data['login']
        password = data['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "not ok"})
    
def change(request):
    pass

def out(request):
    if request.user.is_authenticated:
        logout(request=request)
        return JsonResponse({"status": "ok"})