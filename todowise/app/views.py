from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

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

def student_list(request):
    student = Student.objects.all()
    #student = get_object_or_404(Student.objects.all())
    get_object_or_404(student)
    return render(request, template_name = 'app/student.html', context = {'student_subjects':student})


def add_subject(request, course_id):
    subject_title = request.POST.get('subject_title')
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = Subject(title = subject_title, course = course, user = request.user)
    subject.save()
    return redirect('course_list', course_id = course_id)


def add_grade(request, student_id, subject_id):
    if request.method == 'POST':
        grade_value = request.POST.get('grade')
        student = get_object_or_404(Student, pk=student_id)
        subject = get_object_or_404(Subject, pk=subject_id)

        # Procurar por uma instância de Grade existente ou criar uma nova
        grade, created = Grade.objects.get_or_create(student=student, subject=subject, defaults={'grade': grade_value})

        if not created:
            # Atualizar a nota se já existir
            grade.grade = grade_value
            grade.save()

        # Retornar a nota atualizada em JSON
        return JsonResponse({'grade': grade.grade})


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

def update_grade(request, grade_id):
    if request.method == 'POST':
        new_grade = float(request.POST.get('grade'))
        grade = Grade.objects.get(pk=grade_id)
        grade.grade = new_grade
        grade.save()
    #return redirect('open_subject')  # Redireciona para a página com a lista de notas
    return render(request, 'app/subjects.html')

def update_status(request, student_id):
    student = Student.objects.get(pk=student_id)
    grades = Grade.objects.filter(student=student)

    for grade in grades:
        if all(grade.grade >= 5):
            status = "Aprovado"
        else:
            status = "Reprovado"
    #status = "Aprovado" if all(grade.grade >= 5 for grade in grades) else "Reprovado"
    return render(request, 'subjects.html', context= {'status': status})


def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        # Receba os dados do formulário e atualize a presença do aluno
        attendance.present = request.POST.get('present') == 'True'  # ou False, dependendo do formulário
        attendance.save()
        return redirect('attendance_detail', attendance_id=attendance_id)
    return render(request, 'app/edit_attendance.html', {'attendance': attendance})


def open_subject(request, course_id, subject_id):
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = get_object_or_404(Subject, pk = subject_id, course = course)
    grades = Grade.objects.filter(subject=subject).prefetch_related('student')
    students_grades = []
    for grade in grades:
        student_info = {
            'student': grade.student,
            'grade': grade.grade,
        }
        students_grades.append(student_info)
    return render(request, template_name = 'app/subjects.html', context = {'subject':subject, 'grades':grades})

