from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ('หญิง','หญิง'),
    ('ชาย','ชาย'),
]

class School(models.Model):
    sch_id = models.AutoField(primary_key=True)
    sch_name = models.CharField(max_length=255)
    sch_code_name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_on = models.DateTimeField("date updated", auto_now=True)

class Classroom(models.Model):
    class_id = models.AutoField(primary_key=True)
    sch_id = models.ForeignKey(School,on_delete=models.CASCADE)
    grade = models.IntegerField()
    room = models.IntegerField()
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_on = models.DateTimeField("date updated", auto_now=True)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES)
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_on = models.DateTimeField("date updated", auto_now=True)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES)
    created_at = models.DateTimeField("date created", default=timezone.now)
    updated_on = models.DateTimeField("date updated", auto_now=True)

class TeacherClassroom(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)