from django.contrib import admin
from .models import Class, Student, Attendance


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'student_count', 'created_at']
    search_fields = ['name', 'code', 'description']
    list_filter = ['created_at']
    
    def student_count(self, obj):
        return obj.students.count()
    student_count.short_description = 'Students'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'class_enrolled', 'email', 'created_at']
    search_fields = ['name', 'student_id', 'email']
    list_filter = ['class_enrolled', 'created_at']
    list_select_related = ['class_enrolled']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'class_enrolled', 'date', 'status', 'marked_at']
    search_fields = ['student__name', 'student__student_id', 'class_enrolled__name']
    list_filter = ['status', 'date', 'class_enrolled']
    date_hierarchy = 'date'
    list_select_related = ['student', 'class_enrolled']
