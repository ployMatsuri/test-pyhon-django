from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet


router = DefaultRouter()

router.register(r'schools',SchoolViewSet,basename='school')
router.register(r'classroom',ClassroomViewSet,basename='classroom')

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
