from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Section, Student, Semester, Instructor, Registration, Course, Year, Period

class InstructorInline(admin.StackedInline):
    model = Instructor
    can_delete = False
    verbose_name_plural = 'instructor'


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class StudentAdmin(BaseUserAdmin):
    inlines = (InstructorInline, StudentInline,)

admin.site.unregister(User)
admin.site.register(User, StudentAdmin)


admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Instructor)
admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(Period)