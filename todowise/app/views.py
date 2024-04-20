from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import User, Course, Subject, Student, Grade, Attendance, Register


def index(request):
    if request.user.is_authenticated:
        students_all = Student.objects.all()
        total_students = students_all.count()  # Conta todos os alunos
        total_courses = Course.objects.all().count()
        total_subjects = Subject.objects.all().count()
        total_users = User.objects.all().count()
        context = {
            'students_all': students_all,
            'total_students': total_students,
            'total_courses': total_courses,
            'total_subjects': total_subjects,
            'total_users': total_users}
        return render(request, template_name = 'app/app.html', context = context)
    else:
        return redirect('app_login')


def app_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('app_index')
    return render(request, 'app/login.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')


def course_list(request, course_id):
    #course = Course.objects.get(pk=course_id)
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    return render(request, template_name = 'app/course.html', context = {'course':course})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, template_name = 'app/subject_list.html', context = {'subjects':subjects})

def student_list(request):
    student = Student.objects.all()
    return render(request, template_name = 'app/student.html', context = {'student_subjects':student})

def user_list(request):
    users = User.objects.all()
    #get_object_or_404(users)
    return render(request, template_name = 'app/user.html', context = {'users':users})


def add_subject(request, course_id):
    subject_title = request.POST.get('subject_title')
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = Subject(title = subject_title, course = course, user = request.user)
    subject.save()
    return redirect('course_list', course_id = course_id)


def remove_subject(request, course_id, subject_id):
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = get_object_or_404(Subject, pk = subject_id, course = course)
    subject.delete()
    return redirect('course_list', course_id = course_id)


def done_subject(request, course_id, subject_id):
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = get_object_or_404(Subject, pk = subject_id, course = course)
    if subject.done is True:
        subject.done = False
    else:
        subject.done = True
    # or -> subject.done = not subject.done
    subject.save()
    return redirect('course_list', course_id = course_id)


from django.shortcuts import redirect

def add_grade(request, studend_id, subject_id, grade_id):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        new_grade = float(request.POST.get('grade'))
        student = Student.objects.get(pk=student_id)
        subject_id = request.GET.get('subject_id')
        subject = Subject.objects.get(pk=subject_id)
        # Em seguida, você cria a nota associada ao aluno e à disciplina:
        grade = Grade.objects.create(student=student, subject=subject, grade=new_grade)
        # Seja qual for a maneira que você obtém a disciplina, você cria a nota:
        grade = Grade.objects.create(student=student, grade=new_grade)
        # Redireciona de volta para a página da disciplina após adicionar a nota
        return redirect('open_subject', course_id=subject.course.id, subject_id=subject.id)



def update_grade(request, grade_id):
    if request.method == 'POST':
        new_grade = float(request.POST.get('grade'))
        grade = Grade.objects.get(pk=grade_id)
        grade.grade = new_grade
        grade.save()
        grades = Grade.objects.all()

        return render(request, template_name='app/subjects.html', context={'grades': grades})

def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id, user = request.user)
    if request.method == 'POST':
        # Receba os dados do formulário e atualize a presença do aluno
        attendance.present = request.POST.get('present') == 'True'  # ou False, dependendo do formulário
        attendance.save()
        return redirect('attendance_detail', attendance_id=attendance_id)
    return render(request, 'app/edit_attendance.html', {'attendance': attendance})


def open_subject(request, course_id, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id, user = request.user)
    # Obter todos os registros relacionados à disciplina
    registers = Register.objects.filter(course_id=course_id, subject=subject)
    # Extrair os alunos desses registros
    students = [register.student for register in registers]
    # Obter as notas dos alunos nesta disciplina
    grades = Grade.objects.filter(student__in=students, subject=subject)

    # Verificar e criar Grades para alunos que não possuem Grade nesta disciplina
    for student in students:
        if not grades.filter(student=student).exists():
            Grade.objects.create(subject=subject, student=student)

    # Atualizar a lista de Grades para incluir as novas Grades criadas
    grades = Grade.objects.filter(student__in=students, subject=subject)

    return render(request, template_name='app/subjects.html',
                  context={'subject': subject, 'students': students, 'grades': grades})
