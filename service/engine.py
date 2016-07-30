from .models import *
import random

def chooseVariations(course, student):
    all_variations = course.variation_set.all()
    # Perform chi-square test
    scores=[]
    avg_score=0
    NTot = len(Result.objects.all())
    for i, var in enumerate(all_variations):
        student_list = Result.objects.filter(choice__variation=var)
        N = len(student_list)
        for s in student_list:
            scores.append(s.score / N) 
    pval = .05

    # determine weights

    winner = scores.index(max(scores))
    i=0
    probs=[]
    Nvar = len(all_variations)
    for var in all_variations:
        if i==winner:
            probs.append([var,1-pval+pval/Nvar])
        else:
            probs.append([var,pval/Nvar])
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
    
    variation = weighted_choice(probs)

    print(variation.description)
    
    return Choice.objects.create(variation=variation, student=student)
