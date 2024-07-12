from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
import json
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return render(request, 'yes_reg.html', {'username': request.session.get('username', None)})
    else:
        return render(request, 'no_reg.html')

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
            request.session['username'] = username
            return HttpResponse('True')
