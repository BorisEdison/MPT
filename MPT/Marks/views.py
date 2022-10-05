from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import StudentProfile
from accounts.models import User
from .models import AcademicScores
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='Login')
def studentMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)    
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code').values()
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student}
    return render(request, 'Marks/student-marks.html', context)

@login_required(login_url='Login')
def studentAddMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    context = {'title': 'studentmarks'}
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('studentMarks', pk = user.usr_id)

    return render(request, 'Marks/student-add-marks.html', context)

@login_required(login_url='Login')
def studentEditMarks(request, pk,id):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    context = {'title': 'studentmarks', 'mark':mark}

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']
        try:
            Edit = AcademicScores.objects.get(id = id)
            Edit.student = student
            Edit.academicYear = year
            Edit.sem = sem
            Edit.sub_code = scode
            Edit.exam = exam
            Edit.marks = marks
            Edit.save()
        except:
            pass
        return redirect('studentMarks', pk = user.usr_id)

    return render(request, 'Marks/student-edit-marks.html', context)

@login_required(login_url='Login')
def studentDeleteMarks(request, pk, id):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('studentMarks',pk = user.usr_id)

@staff_member_required(login_url='Login')
def facultyStudentMarks(request,stu_pk):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code').values()
    
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student}

    return render(request, 'Marks/faculty-student-marks.html', context)

@staff_member_required(login_url='Login')
def facultyEditMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)

    context = {'title': 'studentmarks', 'mark':mark}

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']
        try:
            Edit = AcademicScores.objects.get(id = id)
            Edit.student = student
            Edit.academicYear = year
            Edit.sem = sem
            Edit.sub_code = scode
            Edit.exam = exam
            Edit.marks = marks
            Edit.save()      
        except:
            pass  

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-edit-marks.html', context)

@staff_member_required(login_url='Login')
def facultyAddMarks(request,stu_pk):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-add-marks.html')
    
@staff_member_required(login_url='Login')
def facultyDeleteMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('facultyStudentMarks',stu_pk = user.usr_id)

