from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import *
from .engine import *

def index(request):
    template = loader.get_template('service/index.html')
    return HttpResponse(template.render({ 'courses': Course.objects.all() }, request))


def prepare_course(request, course_id):
    template = loader.get_template('service/prepare_course.html')
    course = get_object_or_404(Course, pk=course_id)
    return HttpResponse(template.render({ 'course': course }, request))


def create_student(request, course_id):
    student = Student.objects.get_or_create(**request.POST['student'])
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponseRedirect(reverse('take_course', args=(course_id, student.id)))


def take_course(request, course_id, student_id):
    template = loader.get_template('service/take_course.html')
    student = get_object_or_404(Student, pk=student_id)
    course = get_object_or_404(Course, pk=course_id)
    choice = chooseVariations(course=course, student=student)
    return HttpResponse(template.render({ 'student': student, course: course, choice: choice }, request))


def edit_course(request, course_id):
    template = loader.get_template('service/edit_course.html')
    course = get_object_or_404(Course, pk=course_id)
    return HttpResponse(template.render({ 'course': course }, request))


def save_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    print(request.POST['course'])
    return HttpResponseRedirect(reverse('edit_course', args=(course_id)))
