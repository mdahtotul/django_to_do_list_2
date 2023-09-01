from django.urls import path

from task import views

urlpatterns = [
  path("", views.get_all_tasks, name="all_tasks"),
  path("create/", views.create_task, name="create_task"),
  path("edit/<int:pk>", views.edit_task, name="edit_task"),
  path("delete/<int:pk>", views.delete_task, name="delete_task"),
]