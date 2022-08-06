from datetime import datetime
import django_filters

from api.models import TodoItem

#3 filters - deadline before today, deadline today or after today, deadline not set
#Assign todays date to variable today
#If url contains ?deadline=before today, filter by deadline before today
#If url contains ?deadline=today, filter by deadline today
#If url contains ?deadline=after today, filter by deadline after today
#If url contains ?deadline=not_set, filter by deadline not set
class DeadlineFilter(django_filters.FilterSet):
    today = datetime.now()

class CreationFilter(django_filters.FilterSet):
    '''FilterSet for created_at field in TodoItem model. 
    Pass '''
    start_date = django_filters.DateFilter(field_name='created_at',lookup_expr='lt',label='Created before (mm/dd/yyyy):')
    end_date = django_filters.DateFilter(field_name='created_at',lookup_expr='gt',label='Created after (mm/dd/yyyy):')
    class Meta:
        model = TodoItem
        fields = '__all__'