# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from tasks.dbapi import create_task_object, get_task_all, \
    create_tag_bulk, get_tag_by_task
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
    tasks = []
    tasks_objs = get_task_all()
    for obj in tasks_objs:
        tags = get_tag_by_task(obj)
        tasks.append({'task': obj.as_json(), 'task_tags': list(tags)})
    return JsonResponse({'status': 200, 'tasks': tasks})
