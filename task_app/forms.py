from django import forms

from task_app.models import TaskModel


class TaskForm(forms.ModelForm):

    class Meta:

        model = TaskModel

        fields = ['task_name','priority']

# Because the user should not choose or type their own name in the task form —
# it should be automatically linked to the currently logged-in user.