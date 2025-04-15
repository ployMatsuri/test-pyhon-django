from django_filters import FilterSet, filters
from apis.models import School, Classroom, Teacher, Student
import django_filters


class SchoolFilter(django_filters.FilterSet):
    sch_name = django_filters.CharFilter(field_name='sch_name')

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
        field_name='firstname')
    lastname = django_filters.CharFilter(
        field_name='lastname')
    gender = django_filters.CharFilter(
        field_name='gender'
    )

    class Meta:
        model = Teacher
        fields = []


class StudentFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(
        queryset=School.objects.all(),
        field_name='class_id__sch_id'
    )
    classroom = django_filters.ModelChoiceFilter(
        queryset=Classroom.objects.all(),
        field_name='class_id'
    )
    firstname = django_filters.CharFilter(
        field_name='firstname')
    lastname = django_filters.CharFilter(
        field_name='lastname')
    gender = django_filters.CharFilter(
        field_name='gender')

    class Meta:
        model = Student
        fields = []