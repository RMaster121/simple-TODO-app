from datetime import datetime
import django_filters

from api.models import TodoItem

class CreationFilter(django_filters.FilterSet):
    '''FilterSet for created_at field in TodoItem model.'''
    start_date = django_filters.DateFilter(field_name='created_at',lookup_expr='lt',label='Created before (mm/dd/yyyy):')
    end_date = django_filters.DateFilter(field_name='created_at',lookup_expr='gt',label='Created after (mm/dd/yyyy):')
    deadline_type = django_filters.ChoiceFilter(choices=(('past','Past'),('future','Future'),('none','None')),label='Deadline type:',method='deadline_type_filter')
    def deadline_type_filter(self,queryset,name,value):
        if value == 'past':
            return queryset.filter(due_date__lt=datetime.now())
        elif value == 'future':
            return queryset.filter(due_date__gt=datetime.now())
        else:
            return queryset.filter(due_date__isnull=True)

    class Meta:
        model = TodoItem
        fields = '__all__'
