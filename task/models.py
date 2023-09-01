from django.db import models
from django.contrib.auth.models import User

from task.constants import TASK_PRIORITY, TASK_STATUS, TASK_TO_DO

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=255)
  details = models.TextField(null=True, blank=True)
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
  status = models.CharField(max_length=25, choices=TASK_STATUS, default=TASK_TO_DO)
  due_date = models.DateField(null=True, blank=True)
  priority = models.IntegerField(choices=TASK_PRIORITY, default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)