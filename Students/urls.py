from django.urls import path
from .import views

urlpatterns = [
    

    # students

    path('students/', views.student_list),
    path('students/create/', views.studentcreate),
    path('students/update/<int:pk>/', views.studentupdate),
    path('students/delete/<int:pk>/', views.studentdelete),
    path('students/<int:pk>/', views.studentdetails),


    # courses

    path('courses/', views.course_list), 
    path('courses/create/', views.coursecreate),
    path('courses/update/<int:pk>/', views.courseupdate),
    path('courses/delete/<int:pk>/', views.coursedelete),
    path('courses/<int:pk>/', views.coursedetails),


    # marks

    path('marks/', views.marks_list), 
    path('marks/create/', views.marks_create),
    path('marks/update/<int:pk>/', views.marks_update),
    path('marks/delete/<int:pk>/', views.marks_delete),
    path('marks/<int:pk>/', views.marks_details),
    

    # attendance

    path('attendance/', views.attendance_list), 
    path('attendance/create/', views.attendance_create),
    path('attendance/update/<int:pk>/', views.attendance_update),
    path('attendance/delete/<int:pk>/', views.attendance_delete),
    path('attendance/<int:pk>/', views.attendance_details),
]