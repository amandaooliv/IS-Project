from django import forms
from django.contrib import admin
from .models import User, Course, Subject, Student, Grade, Attendance, Register

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('user__first_name', 'user__last_name')


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
    search_fields = ('course__title', 'course__user')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'user', 'created_at')
    list_filter = ('course', 'user')
    search_fields = ('subject__title', 'subject__course', 'subject__user')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name_student', 'last_name_student', 'birth_date', 'email')
    search_fields = ('student__first_name', 'student__last_name')
    #inlines = [SubjectInline]


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'grade')
    search_fields = ('grade__subject', 'grade__student')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'student', 'present')
    list_filter = ('subject', 'date')
    search_fields = ('attendance__subject', 'attendance__student')


class SubjectInlineForm2(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['course']
        widgets = {
            'title': forms.Select(choices=[(subject.id, subject.title) for subject in Subject.objects.all()])
        }

class SubjectInline2(admin.TabularInline):
    model = Subject
    form = SubjectInlineForm2
    extra = 1

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    inlines = [SubjectInline2]
    list_display = ('course', 'student', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('course__title', 'student__first_name', 'student__last_name')
