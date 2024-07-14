from django.shortcuts import render
import json
from .models import task as Task
from django.http import JsonResponse, HttpResponse

def home(request):
    return render(request, 'home.html')

def new_task(request):
    text = request.POST.get('text')
    task = Task(text=text, status='new')
    task.save
    return HttpResponse('ok')

def list_task(request):
    list_task = Task.objects.all()
    records_dict = {}
    for index, record in enumerate(list_task):
        records_dict[str(index)] = {
            "text": record.text,
            "status": record.status,
            "date": record.date_creation.strftime("%Y-%m-%d %H:%M")
        }
    return JsonResponse(records_dict)


def change_task(request):
    pass

def delete_task(request):
    pass