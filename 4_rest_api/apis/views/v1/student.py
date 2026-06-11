from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from apis.models import Student
from apis.serializers import StudentListSerializer, StudentDetailSerializer
from apis.filters import StudentFilter


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [AllowAny]
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentListSerializer
