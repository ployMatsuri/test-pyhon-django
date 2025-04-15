from rest_framework import serializers
from apis.models import Classroom, TeacherClassroom, Student, Teacher, School  
from django.db.models import Count

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['sch_id', 'sch_name', 'sch_code_name', 'address', 'created_at', 'updated_on']

class SchoolSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['sch_id', 'sch_name', 'sch_code_name', 'address',]
    
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
        return sum(c.teacherclassroom_set.count() for c in obj.classroom_set.all())
    
    def get_student_count(self,obj):
        return sum(s.student_set.count() for s in obj.classroom_set.all())
    
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['class_id', 'sch_id', 'grade', 'room', 'created_at', 'updated_on']

class ClassroomSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['class_id', 'grade', 'room']

class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    
    class Meta:
        model = Classroom
        fields = ['class_id','teachers','students']

    def get_teachers(self, obj):
        classroom_teachers = TeacherClassroom.objects.filter(classroom=obj)
        teachers = [tc.teacher for tc in classroom_teachers]
        return TeacherSimpleSerializer(teachers, many=True).data

    def get_students(self, obj):
        students = Student.objects.filter(class_id=obj)
        return StudentSimpleSerializer(students, many=True).data

class TeacherSerializer(serializers.ModelSerializer):
    classroom_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Teacher
        fields = ['teacher_id', 'firstname', 'lastname', 'gender', 'created_at', 'updated_on', 'classroom_ids']

    def create(self, validated_data):
        classroom_ids = validated_data.pop('classroom_ids', [])
        teacher = Teacher.objects.create(**validated_data)

        for classroom_id in classroom_ids:
            TeacherClassroom.objects.create(teacher=teacher, classroom_id=classroom_id)

        return teacher
    
    def update(self, instance, validated_data):
        classroom_ids = validated_data.pop('classroom_ids', None)
        
        if classroom_ids is not None:
            TeacherClassroom.objects.filter(teacher=instance).delete()
            
            for classroom_id in classroom_ids:
                classroom = Classroom.objects.get(class_id=classroom_id)
                TeacherClassroom.objects.create(teacher=instance, classroom=classroom)
        
        return super().update(instance, validated_data)
    
class TeacherSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'firstname', 'lastname', 'gender']
    
class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['teacher_id', 'classrooms']

    def get_classrooms(self, obj):
        teacher_classrooms = TeacherClassroom.objects.filter(teacher=obj)
        classrooms = [tc.classroom for tc in teacher_classrooms]
        return ClassroomSimpleSerializer(classrooms, many=True).data
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'class_id', 'firstname', 'lastname', 'gender', 'created_at', 'updated_on']

class StudentDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSimpleSerializer(source='class_id', read_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'classrooms']

class StudentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'firstname', 'lastname', 'gender']



