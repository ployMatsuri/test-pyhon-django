from apis.models import Classroom
from rest_framework import viewsets
from apis.serializers import ClassroomSerializer, ClassroomDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apis.filters import ClassroomFilter
from rest_framework.response import Response
from rest_framework import status

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return super().get_serializer_class()