from django.urls import path

from task.views.category import list_category, create_category, edit_category, delete_category
from task.views.task import get_all_tasks, create_task, edit_task, delete_task

urlpatterns = [
  path("", get_all_tasks, name="all_tasks"),
  path("create/", create_task, name="create_task"),
  path("edit/<int:pk>", edit_task, name="edit_task"),
  path("delete/<int:pk>", delete_task, name="delete_task"),
  path("categories/", list_category, name="categories"),
  path("category/create/", create_category, name="create_category"),
  path("category/edit/<int:pk>", edit_category, name="edit_category"),
  path("category/delete/<int:pk>", delete_category, name="delete_category"),
]