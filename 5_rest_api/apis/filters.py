from django_filters import FilterSet, filters
from apis.models import School, Classroom
import django_filters


class SchoolFilter(django_filters.FilterSet):
    sch_name = django_filters.CharFilter(field_name='sch_name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['sch_name']

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), field_name='sch_id')

    class Meta:
        model = Classroom
        fields = ['school']