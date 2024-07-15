from django.shortcuts import render
import json
from list_task.models import Task
from django.http import JsonResponse, HttpResponse

def home(request):
    return render(request, 'home.html')

def new_task(request):
    text = json.loads(request.body)['text']
    new_task = Task(text=text, status='new')
    new_task.save()
    return HttpResponse('ok')

def list_task(request):
    list_task = Task.objects.all()
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