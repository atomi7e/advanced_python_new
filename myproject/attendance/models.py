from django.db import models
from django.utils import timezone


class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='absent')
    notes = models.TextField(blank=True)
    marked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', 'student']
        unique_together = ['student', 'date']
    
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
