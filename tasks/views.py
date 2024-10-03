from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "templates/tasks/task_list.html"
