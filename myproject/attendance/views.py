from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta
from .models import Class, Student, Attendance, Teacher
from .forms import UserRegistrationForm, UserLoginForm, TeacherRegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'attendance/login.html', {'form': form})


def home(request):
    classes = Class.objects.all()
    return render(request, 'attendance/home.html', {'classes': classes})


def class_students(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    students = class_obj.students.all()
    return render(request, 'attendance/class_students.html', {
        'class_obj': class_obj,
        'students': students
    })


def mark_attendance(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    students = class_obj.students.all()
    
    attendance_date = request.GET.get('date', date.today().isoformat())
    try:
        attendance_date = date.fromisoformat(attendance_date)
    except (ValueError, TypeError):
        attendance_date = date.today()
    
    existing_attendance = {}
    students_list = list(students)
    for student in students_list:
        attendance = Attendance.objects.filter(
            student=student,
            date=attendance_date
        ).first()
        if attendance:
            existing_attendance[student.id] = attendance.status
            student.current_status = attendance.status
        else:
            student.current_status = 'absent'
    
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'absent')
            attendance, created = Attendance.objects.update_or_create(
                student=student,
                date=attendance_date,
                defaults={'status': status, 'class_enrolled': class_obj}
            )
        return redirect('attendance_report_date', class_id=class_id, date_str=attendance_date.isoformat())
    
    return render(request, 'attendance/mark_attendance.html', {
        'class_obj': class_obj,
        'students': students_list,
        'attendance_date': attendance_date,
        'existing_attendance': existing_attendance
    })


def attendance_report(request, class_id, date_str=None):
    class_obj = get_object_or_404(Class, id=class_id)
    
    if date_str:
        try:
            report_date = date.fromisoformat(date_str)
        except (ValueError, TypeError):
            report_date = date.today()
    else:
        date_param = request.GET.get('date', date.today().isoformat())
        try:
            report_date = date.fromisoformat(date_param)
        except (ValueError, TypeError):
            report_date = date.today()
    
    attendances = Attendance.objects.filter(
        class_enrolled=class_obj,
        date=report_date
    ).select_related('student')
    
    total_students = class_obj.students.count()
    present_count = attendances.filter(status='present').count()
    absent_count = attendances.filter(status='absent').count()
    late_count = attendances.filter(status='late').count()
    
    return render(request, 'attendance/report.html', {
        'class_obj': class_obj,
        'attendances': attendances,
        'report_date': report_date,
        'total_students': total_students,
        'present_count': present_count,
        'absent_count': absent_count,
        'late_count': late_count,
    })


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendances = Attendance.objects.filter(student=student).select_related('class_enrolled').order_by('-date')
    
    present_count = attendances.filter(status='present').count()
    absent_count = attendances.filter(status='absent').count()
    late_count = attendances.filter(status='late').count()
    
    return render(request, 'attendance/student_detail.html', {
        'student': student,
        'attendances': attendances,
        'present_count': present_count,
        'absent_count': absent_count,
        'late_count': late_count,
    })


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def register_teacher(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create Teacher profile with pending status
            Teacher.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone', ''),
                department=form.cleaned_data.get('department', ''),
                status='pending'
            )
            username = form.cleaned_data.get('username')
            messages.success(
                request, 
                f'Teacher registration submitted for {username}! Your request is pending admin approval. '
                'You will be notified once your registration is reviewed.'
            )
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'attendance/register_teacher.html', {'form': form})
