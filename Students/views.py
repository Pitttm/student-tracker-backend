from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CourseSerializer,StudentSerializer,MarksSerializer,AttendanceSerializer
from .models import Student,Course,Marks,Attendance




# Create your views here.


## Student..................................................

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentdetails(request,pk):
    students = Student.objects.get(id=pk)
    serializer = StudentSerializer(students,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def studentcreate(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def studentupdate(request,pk):
    students = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=students,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def studentdelete(request,pk):
    students = Student.objects.get(id=pk)
    students.delete()

    return Response({"message": "Student deleted successfully"})



## Course.................................................


@api_view(['GET'])
def course_list(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def coursedetails(request,pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def coursecreate(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def courseupdate(request,pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def coursedelete(request,pk):
    courses = Course.objects.get(id=pk)
    courses.delete()

    return Response({"message": " Course deleted successfully"})


## Marks..........................................................


@api_view(['GET'])
def marks_list(request):
    marks = Marks.objects.all()
    serializer = MarksSerializer(marks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def marks_details(request,pk):
    marks = Marks.objects.get(id=pk)
    serializer = MarksSerializer(marks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def marks_create(request):
    serializer = MarksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def marks_update(request,pk):
    students = Marks.objects.get(id=pk)
    serializer = MarksSerializer(instance=students,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def marks_delete(request,pk):
    marks = Marks.objects.get(id=pk)
    marks.delete()

    return Response({"message": "Marks deleted successfully"})



## Attendance..................................................................


@api_view(['GET'])
def attendance_list(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def attendance_details(request,pk):
    attendance = Attendance.objects.get(id=pk)
    serializer = AttendanceSerializer(attendance,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def attendance_create(request):
    serializer = AttendanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def attendance_update(request,pk):
    attendance = Attendance.objects.get(id=pk)
    serializer = AttendanceSerializer(instance=attendance,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def attendance_delete(request,pk):
    attendance = Attendance.objects.get(id=pk)
    attendance.delete()

    return Response({"message": "Attendance deleted successfully"})