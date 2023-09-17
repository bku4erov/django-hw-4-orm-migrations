from django.contrib import admin

from .models import Student, Teacher


class TeachersInline(admin.TabularInline):
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
