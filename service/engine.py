from .models import *


def chooseVariations(course, student):
    all_variations = course.variation_set.all()

    # Perform Fisher test



    # determine weights
    
    # function that makes a weighted random selection
    # http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
           if upto + w >= r:
              return c
           upto += w
        assert False, "Shouldn't get here"
    
    # choose one
    
    variation = all_variations[0]
    
    return Choice.objects.create(variation=variation, student=student)
