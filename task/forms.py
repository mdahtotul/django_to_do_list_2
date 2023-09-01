from django import forms

from task.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "details"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "details": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }
