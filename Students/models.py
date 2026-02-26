from django.db import models
from django.utils.timezone import now

# Create your models here.
class Student(models.Model):
    student_name= models.CharField(max_length=100)
    roll_no= models.CharField(max_length=20,unique= True)
    email= models.EmailField(unique= True)
    year= models.IntegerField()

    def __str__(self):
        return self.student_name
    
    

class Course(models.Model):
    course_name= models.CharField(max_length=100)
    course_code= models.CharField(max_length=20,unique= True)
    semester= models.CharField(max_length=10)

    def __str__(self):
        return self.course_name
    

    
class Marks(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    internal_marks= models.IntegerField()
    external_marks= models.IntegerField()

    class Meta:
        unique_together=('student','course')

    @property
    def total_marks(self): 
        return self.internal_marks + self.external_marks

    def __str__(self):
        return f"{self.student.student_name}-{self.course.course_name}-{self.total_marks}"
    

    
class Attendance(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    date= models.DateField(default=now)
    is_present= models.BooleanField(default=True)

    class Meta:
        unique_together=('student','course','date')

    def __str__(self):
        return f"{self.student.student_name}-{self.course.course_name}-{self.date}"