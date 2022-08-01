from django.db import models
from positions.fields import PositionField

# Create your models here.
class TodoItem(models.Model):
    '''Model representing a todo item'''
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    value = models.TextField(blank=True)

class ListItem(models.Model):
    '''Model representing a list item'''
    value = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    todo_item = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    position = PositionField(collection='todo_item', default=0)

    