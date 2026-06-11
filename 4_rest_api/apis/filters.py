from django_filters import FilterSet, filters
from apis.models import School, Classroom, Teacher, Student


class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(FilterSet):
    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['school', 'classrooms', 'first_name', 'last_name', 'gender']


class StudentFilter(FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']
