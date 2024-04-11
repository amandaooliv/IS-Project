from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import User, List, Item, Student, Grade, Attendance

def index(request):
    if request.user.is_authenticated:
        return render(request, template_name = 'app/app.html')
    else:
        return redirect('app_login')


def app_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('app_index')
    return render(request, 'app/login.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')


def to_do_list(request, list_id):
    #list = List.objects.get(pk=list_id)
    list = get_object_or_404(List, pk = list_id, user = request.user)
    return render(request, template_name = 'app/list.html', context = {'list':list})


def add_item(request, list_id):
    item_title = request.POST.get('item_title')
    list = get_object_or_404(List, pk = list_id, user = request.user)
    item = Item(title = item_title, list = list)
    item.save()
    return redirect('to_do_list', list_id = list_id)


def remove_item(request, list_id, item_id):
    list = get_object_or_404(List, pk = list_id, user = request.user)
    item = get_object_or_404(Item, pk = item_id, list = list)
    item.delete()
    return redirect('to_do_list', list_id = list_id)


def done_item(request, list_id, item_id):
    list = get_object_or_404(List, pk = list_id, user = request.user)
    item = get_object_or_404(Item, pk = item_id, list = list)
    if item.done is True:
        item.done = False
    else:
        item.done = True
    # or -> item.done = not item.done
    item.save()
    return redirect('to_do_list', list_id = list_id)


def edit_student(request, student_id, list_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Receba os dados do formulário e atualize o objeto do aluno
        student.name = request.POST.get('first_name_student')
        student.last_name = request.POST.get('last_name_student')
        student.birth_date = request.POST.get('birth_date')
        student.adress = request.POST.get('adress')
        student.email = request.POST.get('email')
        student.celphone = request.POST.get('celphone')
        student.list = get_object_or_404(List, pk=list_id, user=request.user)
        student.save()

        return redirect('student_detail', student_id=student_id)
    return render(request, 'app/edit_student.html', {'student': student})


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

def open_item(request, list_id, item_id):
    #list = List.objects.get(pk=list_id)
    list = get_object_or_404(List, pk = list_id, user = request.user)
    item = get_object_or_404(Item, pk = item_id, list = list)
    return render(request, template_name = 'app/subjects.html', context = {'item':item})


def count_student(request):
    students_all = Student.objects.all()
    total_students = students_all.count()  # Conta todos os alunos
    context = {
        'students_all': students_all,
        'total_students' : total_students}
    #count_students = Student.objects.all().count()
    return render(request, 'app/app.html', context)


def count_list(request):
    total_lists = List.objects.all().count()
    return render(request, 'app/app.html', context = {'total_lists': total_lists})


def count_item(request):
    total_items = Item.objects.all().count()
    return render(request, 'app/app.html', context = {'total_items': total_items})


def count_user(request):
    total_users = User.objects.all().count()
    return render(request, 'app/app.html', context = {'total_users': total_users})