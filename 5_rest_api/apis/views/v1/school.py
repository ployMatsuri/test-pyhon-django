from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School
from apis.serializers import SchoolSerializer
from apis.filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
