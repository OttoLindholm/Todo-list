from django.views.generic import ListView

from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"
