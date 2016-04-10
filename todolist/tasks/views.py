# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from tasks.dbapi import create_task_object, get_task_all_description, \
    create_tag_bulk, get_tag_all_name_distinct
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
    tasks = list(get_task_all_description())
    tags = list(get_tag_all_name_distinct())
    return JsonResponse({'status': 200, 'tasks': tasks, 'tags': tags})
