#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad <rmad@Vostro-3446>
#
# Distributed under terms of the MIT license.

"""

"""
from tasks.models import Task, Tag


def create_task_object(description='no description'):
    task = Task(description=description)
    task.save()
    return task


def create_tag_object(title, task):
    tag, created = Tag.objects.get_or_create(title=title, task=task)
    return tag


def create_tag_bulk(titles, task):
    tags = []
    for title in titles:
        tag = create_tag_object(title, task)
        tags.append(tag)
    return tags


def get_task_all():
    return Task.objects.all()


def get_task_by_id(task_id):
    return Task.objects.filter(id=task_id)


def get_task_all_description():
    return Task.objects.values_list('description', flat=True)


def get_tag_all():
    return Tag.objects.all()


def get_tag_all_name_distinct():
    return Tag.objects.values_list('title', flat=True).distinct()


def get_tag_by_task(task_obj):
    return Tag.objects.filter(task=task_obj).values_list('title', flat=True)
