from django.shortcuts import render, redirect
import json
from list_task.models import Task
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('aut')

def new_task(request):
    text = json.loads(request.body)['text']
    user = User.objects.get(pk=request.user.id)
    new_task = Task(text=text, status='new', user=user)
    new_task.save()
    return HttpResponse('ok')

def list_task(request):
    user = User.objects.get(pk=request.user.id)
    list_task = Task.objects.filter(user=user)
    records_dict = {}
    for record in list_task:
        records_dict[str(record.id)] = {
            "text": record.text,
            "status": record.status,
            "date": record.date_creation.strftime("%Y-%m-%d %H:%M")
        }
    return JsonResponse(records_dict)

def change_task(request):
    data = json.loads(request.body)
    id_task = int(data['id'])
    new_status = data['status']
    task = Task.objects.get(id=id_task)
    task.status = new_status
    task.save()
    return HttpResponse('ok')

def delete_task(request):
    task_id = json.loads(request.body)['taskId']
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponse('Задача удалена')