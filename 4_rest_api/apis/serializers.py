from rest_framework import serializers
from apis.models import School, Classroom, Teacher, Student


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']


class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return obj.teachers.count()

    def get_student_count(self, obj):
        return obj.students.count()


class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'year', 'section']


class TeacherBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class StudentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender']


class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherBriefSerializer(many=True, read_only=True)
    students = StudentBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'school', 'year', 'section', 'teachers', 'students']


class ClassroomBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section']


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'school', 'first_name', 'last_name', 'gender']


class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'school', 'first_name', 'last_name', 'gender', 'classrooms']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'school', 'classroom', 'first_name', 'last_name', 'gender']


class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomBriefSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'school', 'classroom', 'first_name', 'last_name', 'gender']
