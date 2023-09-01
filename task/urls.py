from django.urls import path

from task.views.category_view import list_category, create_category, edit_category, delete_category
from task.views.task_view import list_task, create_task, edit_task, complete_task, delete_task

urlpatterns = [
  path("", list_task, name="tasks"),
  path("create/", create_task, name="create_task"),
  path("edit/<int:pk>", edit_task, name="edit_task"),
  path("delete/<int:pk>", delete_task, name="delete_task"),
  path("complete/<int:pk>", complete_task, name="done_task"),
  path("categories/", list_category, name="categories"),
  path("category/create/", create_category, name="create_category"),
  path("category/edit/<int:pk>", edit_category, name="edit_category"),
  path("category/delete/<int:pk>", delete_category, name="delete_category"),
]