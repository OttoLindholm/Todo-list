from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")


class ToggleCompleteView(View):
    @staticmethod
    def get(request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect(reverse("tasks:index"))
