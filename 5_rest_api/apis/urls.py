from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet
from apis.views.v1.teacher import TeacherViewSet
from apis.views.v1.student import StudentViewSet


router = DefaultRouter()

router.register(r'schools',SchoolViewSet,basename='school')
router.register(r'classroom',ClassroomViewSet,basename='classroom')
router.register(r'teachers',TeacherViewSet,basename='teacher')
router.register(r'students',StudentViewSet,basename='student')

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
