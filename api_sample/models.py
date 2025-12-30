from django.db import models

class TodosampleModel(models.Model):

    name = models.CharField(max_length=20)

    email = models.CharField(max_length=200)

    task = models.CharField(max_length=20)