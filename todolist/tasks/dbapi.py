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
