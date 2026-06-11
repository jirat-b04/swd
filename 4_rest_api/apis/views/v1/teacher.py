from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from apis.models import Teacher
from apis.serializers import TeacherListSerializer, TeacherDetailSerializer
from apis.filters import TeacherFilter


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [AllowAny]
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherListSerializer
