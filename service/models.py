from django.contrib.auth.models import User
from django.db import models
from markupfield.fields import MarkupField


class Course(models.Model):
    """
    The course a teacher creates to teach a certain subject.
    """
    title = models.CharField(max_length=200)
    description = MarkupField(markup_type='markdown', default="")
    # `variations` from foreign key
    # `tests` from foreign key

    def __str__(self):
        return self.title


class Variation(models.Model):
    """
    One variation of a course's content.
    """
    course = models.ForeignKey(Course)
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.description


class Lesson(models.Model):
    """
    A part of a course variation.
    """
    variation = models.ForeignKey(Variation)
    index = models.IntegerField()
    content = MarkupField(markup_type='markdown')

    class Meta:
        ordering = [ 'index' ]

    def __str__(self):
        return self.variation.course.title + ", lesson " + str(self.index)


class Test(models.Model):
    """
    Multiple choice test.
    """
    course = models.OneToOneField(Course)
    content = MarkupField(markup_type='markdown')
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return "test for course: " + self.course.title


class MotivationSharedCourseTest(models.Model):
    """
    A binary test checking whether the user hit the link to
    share this course with friends.
    """
    course = models.ForeignKey(Course)


class MotivationFinishedCourseTest(models.Model):
    """
    A binary test checking whether the user hit the link to
    share this course with friends.
    """
    course = models.ForeignKey(Course)


class Student(models.Model):
    """
    Information about the demographics and other predictors.
    """
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100, choices=[ ("male", "Male"), ("female", "Female") ])  # "m" or "f" (or do we need to be politically correct?)
    originLanguageCode = models.CharField(max_length=5, default="en")

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
