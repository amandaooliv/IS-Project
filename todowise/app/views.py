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


def edit_student_drop(request, student_id, course_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Receba os dados do formulário e atualize o objeto do aluno
        student.name = request.POST.get('first_name_student')
        student.last_name = request.POST.get('last_name_student')
        student.birth_date = request.POST.get('birth_date')
        student.adress = request.POST.get('adress')
        student.email = request.POST.get('email')
        student.celphone = request.POST.get('celphone')
        student.course = get_object_or_404(Course, pk=course_id, user=request.user)
        student.save()

        #return redirect('edit_student', student_id=student_id)
    return render(request, 'app/student.html', {'student': student})


def add_remove_student_class(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Lógica para adicionar/remover o aluno de uma turma
        # Aqui você precisa decidir como ser á essa lógica com base na estrutura do seu sistema
        # Por exemplo, você pode ter um campo na classe Student que representa as turmas em que o aluno está matriculado
        # E então adicionar ou remover a turma conforme necessário
        pass
    return render(request, 'app/add_remove_student_class.html', {'student': student})


def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        # Receba os dados do formulário e atualize a presença do aluno
        attendance.present = request.POST.get('present') == 'True'  # ou False, dependendo do formulário
        attendance.save()
        return redirect('attendance_detail', attendance_id=attendance_id)
    return render(request, 'app/edit_attendance.html', {'attendance': attendance})


def create_edit_class(request, class_id=None):
    if class_id:
        # Lógica para editar uma turma existente
        pass
    else:
        # Lógica para criar uma nova turma
        pass
    return render(request, 'app/create_edit_class.html')


def add_edit_grade(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Receba os dados do formulário e crie/edit a nota do aluno
        pass
    return render(request, 'app/add_edit_grade.html', {'student': student})

def open_subject(request, course_id, subject_id):
    course = get_object_or_404(Course, pk = course_id, user = request.user)
    subject = get_object_or_404(Subject, pk = subject_id, course = course)
    return render(request, template_name = 'app/subjects.html', context = {'subject':subject})

