from django.contrib import admin
from .models import User, List, Item, Student, Grade, Attendance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'user', 'created_at')
    #inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name_student', 'last_name_student', 'birth_date', 'email', 'list')


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('item', 'student', 'grade')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('item', 'date', 'student', 'present')