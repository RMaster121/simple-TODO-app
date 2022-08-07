from rest_framework import serializers
import django_filters
from api.models import ListItem, TodoItem


class ListItemSerializer(serializers.ModelSerializer):
    '''Serializer for ListItem model'''
    todo_item = serializers.PrimaryKeyRelatedField(
        queryset=TodoItem.objects.all(), required=False, allow_null=True, default=None)

    # Although todo_item is

    class Meta:
        model = ListItem
        fields = ['id', 'value', 'position', 'todo_item']


class TodoItemSerializer(serializers.ModelSerializer):
    '''Serializer for TodoItem model'''
    created_at = django_filters.DateFromToRangeFilter(read_only=True)
    list_items = ListItemSerializer(many= True)


    # Override the default create method to create a new todo item and related list items
    def create(self, validated_data):

        # If type is list, list_items is required.
        # If type is string, text_value is required.
        # If type is url, url_value is required.
        # Else, raise an error.
        if "type" in validated_data:
            if validated_data["type"] == "L":
                if "list_items" not in validated_data:
                    raise serializers.ValidationError("List items are required for list type todo item.")
            elif validated_data["type"] == "T":
                if "text_value" not in validated_data:
                    raise serializers.ValidationError("Text value is required for string type todo item.")
            elif validated_data["type"] == "U":
                if "url_value" not in validated_data:
                    raise serializers.ValidationError("URL value is required for url type todo item.")
            else:
                raise serializers.ValidationError("Type value is incorrect.")
        else:
            raise serializers.ValidationError("Type is required.") 

        list_items_data = validated_data.pop('list_items')
        todo_item = TodoItem.objects.create(**validated_data)

        # Check if type is list and if list_items is not empty
        if todo_item.type == 'L' and len(list_items_data) == 0:
            raise serializers.ValidationError(
                'List items are required for type L.')

        for data in list_items_data:
            data['todo_item'] = todo_item
            ListItem.objects.create(**data)
        return todo_item

    class Meta:
        model = TodoItem
        fields = ('id', 'type', 'title', 'due_date', 'created_at', 'text_value', 'url_value', 'list_items', )