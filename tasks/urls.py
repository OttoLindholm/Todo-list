from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("tags/", views.TagListView.as_view(), name="tags-list"),
]

app_name = "tasks"
