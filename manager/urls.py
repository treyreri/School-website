from django.urls import path

from .views import SchoolInformationUpdateView,OlympiadWinnerCreateView,OlympiadWinnerDeleteView,OlympiadWinnerUpdateView,ExamFileCreateView,ExamFileDeleteView,ExamFileUpdateView, ManagerDashboardView, StudentCreateView,StudentDeleteView,StudentUpdateView,TeacherCreateView,TeacherDeleteView,TeacherUpdateView,ScheduleCreateView,ExamCreateView,ExamDeleteView,ExamUpdateView,ScheduleDeleteView,ScheduleUpdateView
from .views import (
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
)

from .views import (
    ClassCreateView,
    ClassUpdateView,
    ClassDeleteView,
)

app_name = 'manager'

urlpatterns = [
    path(
    'school-information/edit/',
    SchoolInformationUpdateView.as_view(),
    name='school_information_edit'
),
    path(
    'olympiads/create/',
    OlympiadWinnerCreateView.as_view(),
    name='olympiad-create',
),

path(
    'olympiads/<int:pk>/update/',
    OlympiadWinnerUpdateView.as_view(),
    name='olympiad-update',
),

path(
    'olympiads/<int:pk>/delete/',
    OlympiadWinnerDeleteView.as_view(),
    name='olympiad-delete',
),
    path(
    'exam-files/create/',
    ExamFileCreateView.as_view(),
    name='exam-file-create',
),

path(
    'exam-files/<int:pk>/update/',
    ExamFileUpdateView.as_view(),
    name='exam-file-update',
),

path(
    'exam-files/<int:pk>/delete/',
    ExamFileDeleteView.as_view(),
    name='exam-file-delete',
),
    
    path(
        '',
        ManagerDashboardView.as_view(),
        name='dashboard',
    ),
    path(
    'news/create/',
    NewsCreateView.as_view(),
    name='news-create',
),

path(
    'news/<int:pk>/update/',
    NewsUpdateView.as_view(),
    name='news-update',
),

path(
    'news/<int:pk>/delete/',
    NewsDeleteView.as_view(),
    name='news-delete',
),
    path(
    'classes/create/',
    ClassCreateView.as_view(),
    name='class-create',
),

path(
    'classes/<int:pk>/update/',
    ClassUpdateView.as_view(),
    name='class-update',
),

path(
    'classes/<int:pk>/delete/',
    ClassDeleteView.as_view(),
    name='class-delete',
),
path(
    'students/create/',
    StudentCreateView.as_view(),
    name='student-create',
),

path(
    'students/<int:pk>/update/',
    StudentUpdateView.as_view(),
    name='student-update',
),

path(
    'students/<int:pk>/delete/',
    StudentDeleteView.as_view(),
    name='student-delete',
),
path(
    'teachers/create/',
    TeacherCreateView.as_view(),
    name='teacher-create',
),

path(
    'teachers/<int:pk>/update/',
    TeacherUpdateView.as_view(),
    name='teacher-update',
),

path(
    'teachers/<int:pk>/delete/',
    TeacherDeleteView.as_view(),
    name='teacher-delete',
),
path(
    'schedule/create/',
    ScheduleCreateView.as_view(),
    name='schedule-create',
),

path(
    'schedule/<int:pk>/update/',
    ScheduleUpdateView.as_view(),
    name='schedule-update',
),

path(
    'schedule/<int:pk>/delete/',
    ScheduleDeleteView.as_view(),
    name='schedule-delete',
),
path(
    'exams/create/',
    ExamCreateView.as_view(),
    name='exam-create',
),

path(
    'exams/<int:pk>/update/',
    ExamUpdateView.as_view(),
    name='exam-update',
),

path(
    'exams/<int:pk>/delete/',
    ExamDeleteView.as_view(),
    name='exam-delete',
),
]