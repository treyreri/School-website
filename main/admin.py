from django.contrib import admin

from .models import (
    Class,
    Student,
    Teacher,
    News,
    Schedule,
    Exam,
    ExamFile,
    OlympiadWinner,
    SchoolInformation, )


admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(News)


#schedule
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        'school_class',
        'day',
        'lesson_number',
        'subject',
        'start_time',
        'end_time',)

    list_filter = ( 'school_class', 'day', )
    search_fields = ( 'subject',)

    ordering = (
        'school_class',
        'day',
        'lesson_number',)


#exams

class ExamFileInline(admin.TabularInline):
    model = ExamFile
    extra = 1
    fields = ( 'title', 'pdf_file', )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'school_class', 'exam_date', )
    list_filter = (  'school_class', 'exam_date',)
    search_fields = ('title', 'description',)
    inlines = ( ExamFileInline,)


admin.site.register(OlympiadWinner)
admin.site.register(SchoolInformation)