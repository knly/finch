from django.db import models
from markupfield.fields import MarkupField


class Course(models.Model):
    """
    The course a teacher creates to teach a certain subject.
    """
    title = models.CharField(max_length=200)
    # `variations` from foreign key
    # `tests` from foreign key

    def __str__(self):
        return self.title

class Variation(models.Model):
    """
    One variation of a course's content.
    """
    course = models.ForeignKey(Course)
    content = MarkupField(markup_type='markdown')


class Test(models.Model):
    """
    A test to determine the student's success in learning the subject
    """
    course = models.ForeignKey(Course)
    content = MarkupField(markup_type='markdown')


class Student(models.Model):
    """
    Information about the demographics and other predictors.
    """
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=100, choices=[ ("male", "Male"), ("female", "Female") ])  # "m" or "f" (or do we need to be politically correct?)

    def __str__(self):
        return self.name


class Choice(models.Model):
    """
    One specific choice of a course's variations, determined when a student enrolls in a course.
    The existing data is taken into account to choose the variation best suited for this student.
    """
    variation = models.ForeignKey(Variation)
    student = models.ForeignKey(Student)


class Result(models.Model):
    """
    The result of a test.
    Always relates to a specific choice of variations of the course material.
    """
    test = models.ForeignKey(Test)
    choice = models.ForeignKey(Choice)
    score = models.FloatField()
