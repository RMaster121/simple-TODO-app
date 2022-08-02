from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from api.models import ListItem, TodoItem
from api.serializers import ListItemSerializer, TodoItemSerializer
# Create your views here.

class TodoItemViewSet(viewsets.ModelViewSet):
    '''ViewSet for TodoItem model'''
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    '''ViewSet for ListItem model'''
    queryset = ListItem.objects.all()

    serializer_class = ListItemSerializer
