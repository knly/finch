from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django import forms
import datetime

from .models import *
from .engine import *

def index(request):
    template = loader.get_template('service/index.html')
    return HttpResponse(template.render({ 'courses': Course.objects.all() }, request))


class CreateStudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    birthday = forms.DateField(label="Birthday", widget=forms.SelectDateWidget(attrs={ 'class': 'form-control' }))
    gender = forms.ChoiceField(choices=( ("female", "Female"), ("male", "Male"), ("other", "Other") ), widget=forms.Select(attrs={ 'class': 'form-control' }))
    originLanguageCode = forms.CharField(label="Mother tongue", max_length=10, widget=forms.TextInput(attrs={ 'class': 'form-control' }))

def prepare_course(request, course_id):
    template = loader.get_template('service/prepare_course.html')
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        create_student_form = CreateStudentForm(request.POST)
        if create_student_form.is_valid():
            student, _ = Student.objects.get_or_create(**create_student_form.cleaned_data)
            return HttpResponseRedirect(reverse('take_course', args=(course_id, student.id)))

    create_student_form = CreateStudentForm()
    return HttpResponse(template.render({ 'course': course, 'create_student_form': create_student_form }, request))


def take_course(request, course_id, student_id):
    template = loader.get_template('service/take_course.html')

    student = get_object_or_404(Student, pk=student_id)
    course = get_object_or_404(Course, pk=course_id)
    try:
        choice = Choice.objects.get(student=student, variation__course=course)
    except Choice.DoesNotExist:
        choice = chooseVariations(course=course, student=student)
    if request.method == 'POST':
        result = Result.objects.create(test=course.test, choice=choice,
                                       score=calculate_score(
                                           course, request.POST["users_answer"]))
        return HttpResponseRedirect(reverse('visualization', args=(course_id,)))

    try:
        test = Test.objects.get(course=course)
    except Test.DoesNotExist:
        test = None

    return HttpResponse(template.render(
        { 'student': student,
          'course': course,
          'choice': choice,
          'lessons': Lesson.objects.filter(variation=choice.variation),
          'test': test }, request))


def calculate_score(course, users_answer):
    score = 0
    correct_answer = course.test.correct_answer
    print(len(correct_answer))
    for i in range(0, len(correct_answer)):
        if (i < len(users_answer) and users_answer[i] == correct_answer[i]):
            score += 1 / len(correct_answer)
    return score



def edit_course(request, course_id):
    template = loader.get_template('service/edit_course.html')
    course = get_object_or_404(Course, pk=course_id)
    variation_data = list(map(lambda variation: {
        'id': variation.id,
        'description': variation.description,
        'content': Lesson.objects.filter(variation=variation)[0],
    }, Variation.objects.filter(course=course)))
    return HttpResponse(template.render({ 'course': course, 'variations': variation_data }, request))


def save_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    print(request.POST['course'])
    return HttpResponseRedirect(reverse('edit_course', args=(course_id,)))


def visualization(request, course_id):
    template = loader.get_template('service/visualization.html')
    return HttpResponse(template.render({ 'chart': PlotResults('gender',course_id) }, request))
