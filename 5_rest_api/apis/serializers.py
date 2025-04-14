from rest_framework import serializers
from apis.models import Classroom, TeacherClassroom, Student, Teacher, School  
from django.db.models import Count

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['sch_id', 'sch_name', 'sch_code_name', 'address', 'created_at']