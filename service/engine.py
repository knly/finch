from .models import *


def chooseVariations(course, student):
    all_variations = course.variation_set.all()

    # choose one
    variation = all_variations[0]

    return Choice.objects.create(variation=variation, student=student)
