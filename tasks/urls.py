from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("tags/", views.TagListView.as_view(), name="tags-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
    path(
        "tasks/<int:pk>/toggle-complete",
        views.ToggleCompleteView.as_view(),
        name="toggle-complete",
    ),
]

app_name = "tasks"
