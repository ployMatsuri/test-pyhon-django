from django.test import TestCase
from django.urls import reverse
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import School, Classroom, Teacher, Student, TeacherClassroom

class APITestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='admin')

        self.client = APIClient()

        self.client.login(username='admin', password='admin')

        self.school = School.objects.create(
            sch_name="Test School",
            sch_code_name="TS001",
            address="123 Main St."
        )

        self.classroom1 = Classroom.objects.create(
            sch_id=self.school, 
            grade=5, 
            room=1
        )
        
        self.classroom2 = Classroom.objects.create(
            sch_id=self.school, 
            grade=6, 
            room=2
        
        )
        self.teacher = Teacher.objects.create(
            firstname="John", 
            lastname="Doe", 
            gender="ชาย")
        TeacherClassroom.objects.create(
            teacher=self.teacher, 
            classroom=self.classroom1)
        
        self.student = Student.objects.create(
            firstname="Jane", 
            lastname="Doe", 
            gender="หญิง", class_id=self.classroom1)

    # Test School API
    def test_create_school(self):
        data = {
            "sch_name": "New School",
            "sch_code_name": "NS001",
            "address": "456 New Rd."
        }
        response = self.client.post("/api/v1/schools/", data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_school_with_filter(self):
        response = self.client.get("/api/v1/schools/?name=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_school_detail(self):
        response = self.client.get(f"/api/v1/schools/{self.school.sch_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("classroom_count", response.data)
        self.assertIn("teacher_count", response.data)
        self.assertIn("student_count", response.data)

    def test_update_school(self):
        data = {"sch_name": "Updated School"}
        response = self.client.patch(
            f"/api/v1/schools/{self.school.sch_id}/",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_school(self):
        response = self.client.delete(f"/api/v1/schools/{self.school.sch_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # Test Classroom API 
    def test_create_classroom(self):
        data = {
            "sch_id": self.school.sch_id,
            "grade": 3,
            "room": 1
        }
        response = self.client.post("/api/v1/classroom/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_classroom_with_filter(self):
        response = self.client.get(f"/api/v1/classroom/?school={self.school.sch_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_classroom_detail(self):
        response = self.client.get(f"/api/v1/classroom/{self.classroom1.class_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("teachers", response.data)
        self.assertIn("students", response.data)

    def test_update_classroom(self):
        data = {"grade": 5}
        response = self.client.patch(f"/api/v1/classroom/{self.classroom1.class_id}/", data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_classroom(self):
        response = self.client.delete(f"/api/v1/classroom/{self.classroom1.class_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Teacher API 
    def test_create_teacher(self):
        data = {
            "firstname": "ครูใหม่",
            "lastname": "สุขสวัสดิ์",
            "gender": "หญิง",
            "classroom_ids": [self.classroom2.class_id]
        }
        response = self.client.post("/api/v1/teachers/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_teacher_with_filter(self):
        response = self.client.get(f"/api/v1/teachers/?school={self.school.sch_id}&classroom={self.classroom1.class_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_detail(self):
        response = self.client.get(f"/api/v1/teachers/{self.teacher.teacher_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("classrooms", response.data)

    def test_update_teacher(self):
        data = { "classroom_ids": [self.classroom2.class_id] }
        response = self.client.patch(f"/api/v1/teachers/{self.teacher.teacher_id}/", data=json.dumps(data),content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_teacher(self):
        response = self.client.delete(f"/api/v1/teachers/{self.teacher.teacher_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Student API
    def test_create_student(self):
        data = {
            "firstname": "Student",
            "lastname": "One",
            "gender": "ชาย",
            "class_id": self.classroom2.class_id
        }
        response = self.client.post("/api/v1/students/", data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_student_with_filter(self):
        response = self.client.get(f"/api/v1/students/?school={self.school.sch_id}&classroom={self.classroom1.class_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_detail(self):
        response = self.client.get(f"/api/v1/students/{self.student.student_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("classrooms", response.data)

    def test_update_student(self):
        data = {"firstname": "UpdatedName"}
        response = self.client.patch(f"/api/v1/students/{self.student.student_id}/", data=json.dumps(data),content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(f"/api/v1/students/{self.student.student_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
