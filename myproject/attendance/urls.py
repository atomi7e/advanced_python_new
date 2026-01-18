from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/<int:class_id>/', views.class_students, name='class_students'),
    path('class/<int:class_id>/mark/', views.mark_attendance, name='mark_attendance'),
    path('class/<int:class_id>/report/', views.attendance_report, name='attendance_report'),
    path('class/<int:class_id>/report/<str:date_str>/', views.attendance_report, name='attendance_report_date'),
    
    path('api/attendance/', api_views.api_attendance_list, name='api_attendance_list'),
    path('api/attendance/mark/', api_views.api_mark_attendance, name='api_mark_attendance'),
]

