from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from apis.models import Classroom
from apis.serializers import ClassroomListSerializer, ClassroomDetailSerializer
from apis.filters import ClassroomFilter


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    permission_classes = [AllowAny]
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomListSerializer
