from django.db import models

# Create your models here.

from user_app.models import User

class TaskModel(models.Model):

    priority_choice = [('high','high'),
                       ('low','low')]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    task_name = models.CharField(max_length=50)

    priority = models.CharField(max_length=50,choices=priority_choice)

    created_date = models.DateTimeField(auto_now_add=True)

    is_complete = models.BooleanField(default=False)