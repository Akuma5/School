from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """Information about courses"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

