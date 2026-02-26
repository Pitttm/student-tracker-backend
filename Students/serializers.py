from rest_framework import serializers
from .models import Student,Course,Marks,Attendance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'


class MarksSerializer(serializers.ModelSerializer):
    student_name= serializers.CharField(source='student.student_name',read_only=True)
    course_name= serializers.CharField(source='course.course_name',read_only=True)
    total_marks= serializers.ReadOnlyField()
    class Meta:
        model= Marks
        fields='__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    student_name= serializers.CharField(source='student.student_name',read_only=True)
    course_name= serializers.CharField(source='course.course_name',read_only=True)
    class Meta:
        model= Attendance
        fields='__all__'