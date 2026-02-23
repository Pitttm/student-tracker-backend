from django.contrib import admin

from .models import Student
from .models import Course
from .models import Marks
from .models import Attendance

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Marks)
admin.site.register(Attendance)
