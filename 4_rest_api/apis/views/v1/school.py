from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from apis.models import School
from apis.serializers import SchoolListSerializer, SchoolDetailSerializer
from apis.filters import SchoolFilter


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    permission_classes = [AllowAny]
    filterset_class = SchoolFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolListSerializer
