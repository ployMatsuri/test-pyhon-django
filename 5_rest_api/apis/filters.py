from django_filters import FilterSet, filters
from apis.models import School
import django_filters


class SchoolFilter(django_filters.FilterSet):
    sch_name = django_filters.CharFilter(field_name='sch_name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['sch_name']
