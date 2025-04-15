from rest_framework import serializers
from apis.models import Classroom, TeacherClassroom, Student, Teacher, School  
from django.db.models import Count

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['sch_id', 'sch_name', 'sch_code_name', 'address', 'created_at', 'updated_on']
    
class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['sch_name', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classroom_set.count()
    
    def get_teacher_count(self,obj):
        return sum(c.teacher_classroom_set.cout() for c in obj.classroom_set.all())
    
    def get_student_count(self,obj):
        return sum(s.student_set.count() for s in obj.classroom_set.all())