from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class List(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

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
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='student_items')

    def __str__(self):
        return f'{self.first_name_student} {self.last_name_student}'


class Item(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (done={self.done})'


class Grade(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.student} - {self.item} - {self.grade}'


class Attendance(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student} - {self.item} - {self.date} - Present: {self.present}'

