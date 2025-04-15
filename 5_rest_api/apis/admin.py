from django.contrib import admin
from apis.models import School, Classroom, Teacher, Student, TeacherClassroom

@admin.register(School)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sch_id', 'sch_name', 'sch_code_name', 'address']
    search_fields = ['sch_name', 'address']

@admin.register(Classroom)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['class_id', 'grade', 'room', 'sch_id']
    search_fields = ['class_id']
    list_filter = ['grade', 'sch_id']

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['teacher_id', 'firstname', 'lastname', 'gender']
    search_fields = ['firstname', 'lastname']
    list_filter = ['gender']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'firstname', 'lastname', 'gender', 'class_id']
    search_fields = ['firstname', 'lastname']
    list_filter = ['gender', 'class_id']

@admin.register(TeacherClassroom)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'classroom', 'teacher']
    search_fields = ['classroom', 'teacher']
    list_filter = ['classroom', 'teacher']
