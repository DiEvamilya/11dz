from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from musicschool.models import Student


def student_list_view(request):
    context = {'student_list': Student.objects.all()}
    return render(request, 'student_list.html', context)

def detail_view(request, student_slug):
    student = Student.objects.get(slug=student_slug)
    context = {'student': student}

    return render(request, 'detail.html', context)


def create_view(request):
    context = {'student_list': Student.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        instrument = request.POST.get('instrument')
        average_grade = request.POST.get('average_grade')
        payment = request.POST.get('payment')

        #
        # for field in ['name', 'surname', 'age', 'payment']:
        #     if not request.POST.get(field):
        #         return HttpResponseBadRequest(f"{field} is required.")


        student = Student()
        student.name = name
        student.surname = surname
        student.age = age
        student.course = course
        student.instrument = instrument
        student.average_grade = average_grade
        student.payment = payment

        student.save()

    return render(request, "create.html", context)



def update_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.instrument = request.POST.get('instrument')
        student.average_grade = request.POST.get('average_grade')
        student.payment = request.POST.get('payment')

      
        student.save()
    return render(request, 'update.html', {'student': student})






