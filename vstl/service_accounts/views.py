from django.shortcuts import render
import json
from django.http import JsonResponse
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
        rememberMe = data['rememberMe']
        
        uniqueness = User.objects.filter(username=username).count()
        
        if uniqueness < 1: # Проверка уникальности "логина"
            user = User.objects.create_user(username=username, email=email, password=password) # Регестрация пользователя
            if user is not None:
                login(request, user)
                if rememberMe == False:
                    request.session.set_expiry(0)
                return JsonResponse({"status": "ok"})
            return JsonResponse({"status": "not ok"})
        else:
            return JsonResponse({"status": "login_not_unique"})

def authorization(request):
    if request.method == 'GET':
        return render(request, 'aut.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        username = data['login']
        password = data['password']
        rememberMe = data['rememberMe']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if rememberMe == False:
                request.session.set_expiry(0)
            return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "not ok"})

def change(request):
    if request.method == 'GET':
        return render(request, 'cha.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        password = data['password']
        username = data['login']
        
        user = User.objects.get(pk=request.user.id)
        if password is not None:
            user.set_password(password)  # Corrected usage of set_password method
        if username is not None:
            user.username = username
        user.save()  # Added parentheses to properly call the save method
        login(request, user)
        return JsonResponse({"status": "ok"})

def delete(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        user.delete()
        return JsonResponse({"status": "ok"})
    
    return JsonResponse({"status": "not ok"})

def out(request):
    if request.user.is_authenticated:
        logout(request=request)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "not ok"})