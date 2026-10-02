from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=10)
    grade = models.PositiveSmallIntegerField()
    letter = models.CharField(max_length=1)
    def __str__(self):
        return self.name 

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_class = models.ForeignKey( Class, on_delete=models.CASCADE, related_name='students',)
    photo = models.ImageField( upload_to='students/', blank=True, null=True,)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    school_class = models.ForeignKey( Class, on_delete=models.CASCADE, related_name='teachers',)
    photo = models.ImageField( upload_to='teachers/', blank=True, null=True,)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField( upload_to='news/', blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Schedule(models.Model):
    class Day(models.TextChoices):
        MONDAY = 'MONDAY', 'Понедельник'
        TUESDAY = 'TUESDAY', 'Вторник'
        WEDNESDAY = 'WEDNESDAY', 'Среда'
        THURSDAY = 'THURSDAY', 'Четверг'
        FRIDAY = 'FRIDAY', 'Пятница'
        SATURDAY = 'SATURDAY', 'Суббота'

    school_class = models.ForeignKey( Class, on_delete=models.CASCADE, related_name='schedule',)
    day = models.CharField( max_length=20, choices=Day.choices, )
    lesson_number = models.PositiveSmallIntegerField()
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return f'{self.school_class} - {self.subject}'


class Exam(models.Model):
    title = models.CharField(max_length=200)
    school_class = models.ForeignKey( Class, on_delete=models.CASCADE, related_name='exams',)
    exam_date = models.DateField()
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

from django.core.validators import FileExtensionValidator
class ExamFile(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='files' )

    title = models.CharField(max_length=200)

    pdf_file = models.FileField(
        upload_to='exams/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'jpg', 'jpeg', 'png']
            )
        ] )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OlympiadWinner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_class = models.ForeignKey( Class, on_delete=models.CASCADE, related_name='olympiad_winners',)
    olympiad_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    place = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    photo = models.ImageField( upload_to='olympiads/', blank=True, null=True, )
    description = models.TextField(blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class SchoolInformation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(
        upload_to='school/',
        blank=True,
        null=True,)

    def __str__(self):
        return self.title