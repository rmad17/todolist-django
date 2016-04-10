# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from tasks.dbapi import create_task_object, get_task_all, create_tag_bulk
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
# from tasks.serializers import TaskSerializer, TagSerializer


# Create your views here.
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        task = create_task_object(received_data['description'])
        create_tag_bulk(received_data['tags'], task)
        return JsonResponse({'status': 200})
    return HttpResponse(status=403)


@csrf_exempt
def get_tasks(request):
    task_objects = get_task_all()
    tasks = []
    for obj in task_objects:
        tasks.append(obj.as_json())
    return JsonResponse({'status': 200, 'tasks': tasks})
