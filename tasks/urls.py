#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad <rmad@Vostro-3446>
#
# Distributed under terms of the MIT license.

"""

"""

from django.conf.urls import url
from tasks.views import create_task, get_tasks

urlpatterns = [
    url(r'^task/', create_task),
    url(r'^get_tasks/', get_tasks),
]
