from django.db import models
from positions.fields import PositionField

# Create your models here.


class TodoItem(models.Model):
    '''Model representing a todo item'''
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=(
        ('T', 'String'), ('L', 'List'), ('U', 'URL')))
    title = models.CharField(max_length=200, blank=False, null=False)
    due_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    text_value = models.TextField(blank=True, max_length=500)
    url_value = models.URLField(blank=True)  # TODO: add validator/test it


class ListItem(models.Model):
    '''Model representing a list item'''
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    todo_item = models.ForeignKey(TodoItem, on_delete=models.CASCADE, related_name = "list_items")
    position = PositionField(default=0, unique_for_fields=('todo_item',))
