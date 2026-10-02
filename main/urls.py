from django.urls import path

from .views import (
    HomeView,
    AboutView,
    ClassListView,
    ClassDetailView,
    StudentListView,
    TeacherListView,
    ScheduleListView,
    NewsDetailView,
    NewsListView,
    ExamDetailView,
    ExamListView,
    ExamFileDownloadView,
    OlympiadWinnerListView,
    OlympiadWinnerDetailView,
    SearchView,
)

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),

    path('schedule/', ScheduleListView.as_view(), name='schedule'),

    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),

    path(
        'exams/files/<int:pk>/download/',
        ExamFileDownloadView.as_view(),
        name='exam-file-download',
    ),

    path(
        'olympiads/',
        OlympiadWinnerListView.as_view(),
        name='olympiads',
    ),

    path(
        'olympiads/<int:pk>/',
        OlympiadWinnerDetailView.as_view(),
        name='olympiad-detail',
    ),

    path('search/', SearchView.as_view(), name='search'),
]