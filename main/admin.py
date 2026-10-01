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
    SchoolInformation,
)


admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(News)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        'school_class',
        'day',
        'lesson_number',
        'subject',
        'start_time',
        'end_time',
    )

    list_filter = (
        'school_class',
        'day',
    )

    search_fields = (
        'subject',
    )

    ordering = (
        'school_class',
        'day',
        'lesson_number',
    )


admin.site.register(Exam)
admin.site.register(ExamFile)
admin.site.register(OlympiadWinner)
admin.site.register(SchoolInformation)