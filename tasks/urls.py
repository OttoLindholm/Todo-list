from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("tags/", views.TagListView.as_view(), name="tags-list"),
    path(
        "tasks/<int:pk>/toggle-complete",
        views.ToggleCompleteView.as_view(),
        name="toggle-complete"
    ),
]

app_name = "tasks"
