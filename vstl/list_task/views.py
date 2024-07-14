from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def new_task(request):
    pass

def list_task(request):
    pass

def change_task(request):
    pass

def delete_task(request):
    pass