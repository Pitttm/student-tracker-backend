from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    roll_no= models.CharField(max_length=20,unique= True)
    email= models.EmailField(unique= True)
    year= models.IntegerField()

    def __str__(self):
        return self.name
    
    

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

    @property
    def total_marks(self): 
        return self.internal_marks + self.external_marks

    def __str__(self):
        return f"{self.student.name}-{self.course.course_name}-{self.total_marks}"
    

    
class Attendance(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    attendance_percentage= models.FloatField()

    def __str__(self):
        return f"{self.student.name}-{self.course.course_name}-{self.attendance_percentage}"