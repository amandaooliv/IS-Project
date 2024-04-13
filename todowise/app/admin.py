from django.contrib import admin
from .models import User, Course, Subject, Student, Grade, Attendance, Register

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')


#class StudentInline(admin.TabularInline):
#    model = Student
#    extra = 1

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [SubjectInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'user', 'created_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name_student', 'last_name_student', 'birth_date', 'email')
    #inlines = [SubjectInline]


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'grade')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'student', 'present')

#@admin.register(Register)
#class RegisterAdmin(admin.ModelAdmin):
    #inlines = [SubjectInline]


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('course__title', 'student__first_name', 'student__last_name')
    #inlines = [SubjectInline]
