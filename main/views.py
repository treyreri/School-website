from pathlib import Path

from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import (
    Class,
    Student,
    Teacher,
    News,
    Schedule,
    Exam,
    ExamFile,
    OlympiadWinner,
    SchoolInformation,
)


class HomeView(TemplateView):
    template_name = 'main/home.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = SchoolInformation.objects.first()
        return context


class ClassListView(ListView):
    model = Class
    template_name = 'classes/class_list.html'
    context_object_name = 'classes'


class ClassDetailView(DetailView):
    model = Class
    template_name = 'classes/class_detail.html'
    context_object_name = 'school_class'

    def get_queryset(self):
        return Class.objects.prefetch_related('students')


class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule/schedule.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        queryset = Schedule.objects.select_related('school_class')

        class_id = self.request.GET.get('class')
        day = self.request.GET.get('day')

        if class_id:
            queryset = queryset.filter(school_class_id=class_id)

        if day:
            queryset = queryset.filter(day=day)

        return queryset.order_by(
            'school_class',
            'day',
            'lesson_number',
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['days'] = Schedule.Day.choices
        return context


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.order_by('-created_at')


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class ExamListView(ListView):
    model = Exam
    template_name = 'exams/exam_list.html'
    context_object_name = 'exams'

    def get_queryset(self):
        return Exam.objects.select_related(
            'school_class'
        ).order_by('exam_date')


class ExamDetailView(DetailView):
    model = Exam
    template_name = 'exams/exam_detail.html'
    context_object_name = 'exam'


class ExamFileDownloadView(View):
    def get(self, request, pk):
        exam_file = get_object_or_404(ExamFile, pk=pk)

        original_name = Path(
            exam_file.pdf_file.name
        ).name

        return FileResponse(
            exam_file.pdf_file.open('rb'),
            as_attachment=True,
            filename=original_name,
        )


class OlympiadWinnerListView(ListView):
    model = OlympiadWinner
    template_name = 'olympiads/winner_list.html'
    context_object_name = 'winners'

    def get_queryset(self):
        return OlympiadWinner.objects.select_related(
            'school_class'
        ).order_by('-year', 'place')


class OlympiadWinnerDetailView(DetailView):
    model = OlympiadWinner
    template_name = 'olympiads/winner_detail.html'
    context_object_name = 'winner'


class SearchView(ListView):
    template_name = 'main/search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        return News.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )