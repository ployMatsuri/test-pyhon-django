from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Student
from apis.serializers import StudentSerializer, StudentDetailSerializer
from apis.filters import StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return super().get_serializer_class()