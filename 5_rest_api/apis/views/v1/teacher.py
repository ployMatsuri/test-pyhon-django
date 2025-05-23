from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Teacher
from apis.serializers import TeacherSerializer, TeacherDetailSerializer
from apis.filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return super().get_serializer_class()