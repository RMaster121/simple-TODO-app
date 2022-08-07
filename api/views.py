from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import CreationFilter

from api.models import ListItem, TodoItem
from api.serializers import ListItemSerializer, TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    '''ViewSet for TodoItem model. Searchable by value and value of list_items.'''
    queryset = TodoItem.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = CreationFilter
    serializer_class = TodoItemSerializer
    search_fields = ['text_value', 'list_items__value']
    ordering_fields = ['created_at']
    filterset_fields = ['type', 'due_date']
    
class ListItemViewSet(viewsets.ModelViewSet):
    '''ViewSet for ListItem model'''
    queryset = ListItem.objects.all()

    serializer_class = ListItemSerializer
