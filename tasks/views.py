from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 3


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"
    paginate_by = 7


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ToggleCompleteView(View):
    @staticmethod
    def get(request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect(reverse("tasks:index"))
