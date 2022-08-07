from datetime import datetime
import django_filters

from api.models import TodoItem

class CreationFilter(django_filters.FilterSet):
    '''FilterSet for created_at field in TodoItem model.'''
    start_date = django_filters.DateFilter(field_name='created_at',lookup_expr='lt',label='Created before (mm/dd/yyyy):')
    end_date = django_filters.DateFilter(field_name='created_at',lookup_expr='gt',label='Created after (mm/dd/yyyy):')
    class Meta:
        model = TodoItem
        fields = '__all__'