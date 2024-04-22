from django import forms
from django.contrib import admin
from .models import User, Course, Subject, Student, Grade, Attendance, Register

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name','email')



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
    list_display = ('first_name_student', 'last_name_student', 'registration' ,'birth_date', 'email')
    search_fields = ('first_name_student', 'last_name_student', 'adress', 'email', 'celphone', 'registration')
    #inlines = [SubjectInline]


class GradeAdminForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        subject = cleaned_data.get('subject')

        if student and subject:
            if not student.registers.filter(subject=subject).exists():
                raise forms.ValidationError("Student is not registered on this subject.")

        return cleaned_data


@admin.register(Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    form = GradeAdminForm
    list_display = ('subject', 'student', 'grade', 'status')


class AttendanceAdminForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        subject = cleaned_data.get('subject')

        if student and subject:
            if not student.registers.filter(subject=subject).exists():
                raise forms.ValidationError("Student is not registered on this subject.")

        return cleaned_data


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceAdminForm
    list_display = ('subject', 'date', 'student', 'present')
    list_filter = ('subject', 'date')
    search_fields = ('date', 'present')


class RegisterAdminForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

    # Adiciona o campo de seleção de Subject
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False, label='Subject')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se um course foi selecionado no formulário
        if 'course' in self.data:
            try:
                # Filtra os subjects com base no course selecionado
                course_id = int(self.data.get('course'))
                self.fields['subject'].queryset = Subject.objects.filter(course_id=course_id)
            except (ValueError, TypeError):
                pass  # Se não for possível converter para um inteiro, ou course não existir, não filtra

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'student', 'created_at')
    form = RegisterAdminForm

    def save_model(self, request, obj, form, change):
        # Se um Subject foi selecionado no formulário
        if form.cleaned_data.get('subject'):
            # Associa o Subject ao Register
            obj.subject = form.cleaned_data['subject']
        # Salva o Register
        super().save_model(request, obj, form, change)