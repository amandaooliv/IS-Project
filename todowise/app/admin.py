from django import forms
from django.contrib import admin
from .models import User, Course, Subject, Student, Grade, Attendance, Register

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name','email')


#class StudentInline(admin.TabularInline):
#    model = Student
#    extra = 1

#class SubjectInline(admin.TabularInline):
#    model = Subject
#    extra = 1

class SubjectInlineForm1(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['register']

class SubjectInline1(admin.TabularInline):
    model = Subject
    form = SubjectInlineForm1
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [SubjectInline1]
    #search_fields = ('title')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'user')
    list_filter = ('course', 'user')
    #search_fields = ('title')
    fields = ('title', 'course', 'user')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name_student', 'last_name_student', 'birth_date', 'email')
    search_fields = ('first_name_student', 'last_name_student', 'adress', 'email', 'celphone', 'registration')
    #inlines = [SubjectInline]


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'grade')
    #search_fields = ('grade')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'student', 'present')
    list_filter = ('subject', 'date')
    search_fields = ('date', 'present')


class SubjectInlineForm2(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'course', 'user']
        widgets = {
            'title': forms.Select(choices=[(subject.title, subject.title) for subject in Subject.objects.all()])
        }

class SubjectInline2(admin.TabularInline):
    model = Subject
    form = SubjectInlineForm2
    extra = 1

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    inlines = [SubjectInline2]
    list_display = ('course', 'student', 'created_at')
