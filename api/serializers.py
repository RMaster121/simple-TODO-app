from rest_framework import serializers

from api.models import ListItem, TodoItem

class ListItemSerializer(serializers.ModelSerializer):
    '''Serializer for ListItem model'''
    todo_item_id = serializers.PrimaryKeyRelatedField(queryset=TodoItem.objects.all(), source='todo_item')
    class Meta:
        model = ListItem
        fields = ['id', 'value', 'position', 'todo_item_id']
        

class TodoItemSerializer(serializers.ModelSerializer):
    '''Serializer for TodoItem model'''
    list_items = ListItemSerializer(many=True, read_only=True, source='list_items_set')
    class Meta:
        model = TodoItem
        fields = '__all__'
    
