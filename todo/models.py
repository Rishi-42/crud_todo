from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    # num = models.AutoField()
    task = models.CharField(max_length=1000)

    def __str__(self):
        return self.task
    
    def get_absolute_url(self):
        return reverse('todo:todo_edit', kwargs={
            'pk' :self.pk
        })