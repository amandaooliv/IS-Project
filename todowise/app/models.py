from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f'{self.title}'


class Student(models.Model):
    registration = models.CharField(max_length=20, primary_key=True)
    first_name_student = models.CharField(max_length=100)
    last_name_student = models.CharField(max_length=100)
    birth_date = models.DateField()
    adress = models.CharField(max_length=255)
    email = models.EmailField()
    celphone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name_student} {self.last_name_student}'



class Subject(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects', null=True)
    #register = models.ForeignKey(Register, on_delete=models.CASCADE, default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title})'

class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registers')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course} {self.student}'


class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10,
                              choices=[('Approved', 'Approved'), ('Repproved', 'Repproved'), ('No grade', 'No grade')],
                              blank=True, null=True)

    def save(self, *args, **kwargs):

        # Verifica se já existe uma instância de Grade para o aluno e a matéria
        existing_grade = Grade.objects.filter(subject=self.subject, student=self.student).first()
        if existing_grade:
            # Se existir, atualiza a instância existente com a nova nota e status
            existing_grade.grade = self.grade

        # Calcula o status com base na nova nota
        if self.grade is None:
            self.status = 'No grade'
        elif self.grade >= 5:
            self.status = 'Approved'
        else:
            self.status = 'Repproved'

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.grade}'


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.date} - Present: {self.present}'

