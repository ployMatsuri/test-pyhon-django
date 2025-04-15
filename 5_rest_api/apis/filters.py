from django_filters import FilterSet, filters
from apis.models import School, Classroom, Teacher, Student
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

class TeacherFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(
        queryset=School.objects.all(),
        field_name='teacherclassroom__classroom__sch_id'
    )
    classroom = django_filters.ModelChoiceFilter(
        queryset=Classroom.objects.all(),
        field_name='teacherclassroom__classroom'
    )
    firstname = django_filters.CharFilter(
        field_name='firstname', lookup_expr='icontains'
    )
    lastname = django_filters.CharFilter(
        field_name='lastname', lookup_expr='icontains'
    )
    gender = django_filters.CharFilter(
        field_name='gender', lookup_expr='iexact'
    )

    class Meta:
        model = Teacher
        fields = []