from django import forms
from django_filters.widgets import RangeWidget

from task.models import Category, Task


class CreateTaskCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "details", 'category', 'assigned_to', 'status', 'due_date', 'reminder', 'priority']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "details": forms.Textarea(  # Use Textarea widget for the details field
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5",
                    "rows": 4,  # Adjust the number of rows as needed
                }
            ),
            "category": forms.Select(  # Use Select widget for the category field
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "assigned_to": forms.Select(  # Use Select widget for the assigned_to field
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "status": forms.Select(  # Use Select widget for the status field
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5",
                    "type": "date",  # Use the date input type
                }
            ),
            "reminder": forms.DateTimeInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5",
                    "type": "datetime-local",  # Use the date input type
                }
            ),
            "priority": forms.Select(  # Use Select widget for the priority field
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }

