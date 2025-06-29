import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    """FilterSet for task model to filter by priority, ..etc"""
    due_date_after = django_filters.DateFilter(field_name='due_date', lookup_expr='gte')
    due_date_before = django_filters.DateFilter(field_name='due_date', lookup_expr='lte')
    priority = django_filters.ChoiceFilter(field_name='priority', choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    completed = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['priority', 'completed', 'due_date_after', 'due_date_before']