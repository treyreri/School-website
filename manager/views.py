from django.views.generic import TemplateView

from .mixins import ManagerRequiredMixin


class ManagerDashboardView(
    ManagerRequiredMixin,
    TemplateView
):
    template_name = 'manager/dashboard.html'

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)

from main.models import News

class NewsCreateView(ManagerRequiredMixin, CreateView):
    model = News
    fields = [
        'title',
        'content',
        'image',
    ]
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:news-list')


class NewsUpdateView(ManagerRequiredMixin, UpdateView):
    model = News
    fields = [
        'title',
        'content',
        'image',
    ]
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:news-list')


class NewsDeleteView(ManagerRequiredMixin, DeleteView):
    model = News
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:news-list')


from main.models import Class
class ClassCreateView(ManagerRequiredMixin, CreateView):
    model = Class
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:class-list')


class ClassUpdateView(ManagerRequiredMixin, UpdateView):
    model = Class
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:class-list')


class ClassDeleteView(ManagerRequiredMixin, DeleteView):
    model = Class
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:class-list')


from main.models import Student
class StudentCreateView(ManagerRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:student-list')


class StudentUpdateView(ManagerRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:student-list')


class StudentDeleteView(ManagerRequiredMixin, DeleteView):
    model = Student
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:student-list')

from main.models import Teacher
class TeacherCreateView(ManagerRequiredMixin, CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:teacher-list')


class TeacherUpdateView(ManagerRequiredMixin, UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:teacher-list')


class TeacherDeleteView(ManagerRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:teacher-list')


from main.models import Schedule
class ScheduleCreateView(ManagerRequiredMixin, CreateView):
    model = Schedule
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:schedule')


class ScheduleUpdateView(ManagerRequiredMixin, UpdateView):
    model = Schedule
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:schedule')


class ScheduleDeleteView(ManagerRequiredMixin, DeleteView):
    model = Schedule
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:schedule')



from main.models import Exam
class ExamCreateView(ManagerRequiredMixin, CreateView):
    model = Exam
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:exam-list')


class ExamUpdateView(ManagerRequiredMixin, UpdateView):
    model = Exam
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:exam-list')


class ExamDeleteView(ManagerRequiredMixin, DeleteView):
    model = Exam
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:exam-list')


from main.models import ExamFile
class ExamFileCreateView(ManagerRequiredMixin, CreateView):
    model = ExamFile
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:exam-list')


class ExamFileUpdateView(ManagerRequiredMixin, UpdateView):
    model = ExamFile
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:exam-list')


class ExamFileDeleteView(ManagerRequiredMixin, DeleteView):
    model = ExamFile
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:exam-list')

from main.models import OlympiadWinner
class OlympiadWinnerCreateView(ManagerRequiredMixin, CreateView):
    model = OlympiadWinner
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:olympiads')


class OlympiadWinnerUpdateView(ManagerRequiredMixin, UpdateView):
    model = OlympiadWinner
    fields = '__all__'
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:olympiads')


class OlympiadWinnerDeleteView(ManagerRequiredMixin, DeleteView):
    model = OlympiadWinner
    template_name = 'manager/confirm_delete.html'
    success_url = reverse_lazy('main:olympiads')

from main.models import SchoolInformation
class SchoolInformationUpdateView(ManagerRequiredMixin, UpdateView):
    model = SchoolInformation
    fields = [
        'title',
        'description',
        'address',
        'phone',
        'email',
        'image',
    ]
    template_name = 'manager/form.html'
    success_url = reverse_lazy('main:about')

    def get_object(self, queryset=None):
        return SchoolInformation.objects.first()

