from .models import *
import random
import scipy.stats
from chartit import DataPool,Chart

def chooseVariations(course, student):
    all_variations = course.variation_set.all()
    # Perform chi-square test
    scores=[]
    avg_score=0
    NTot = len(Result.objects.all())
    if NTot == 0:
        variation = random.choice(all_variations)
        return Choice.objects.create(variation=variation,student=student)
    for i, var in enumerate(all_variations):
        student_list = Result.objects.filter(choice__variation=var)
        N = len(list(student_list))
        for s in student_list:
            avg_score += s.score / N
        scores.append(avg_score)
        avg_score=0
    pval = scipy.stats.chisquare(scores)[1]

    # determine weights

    winner = scores.index(max(scores))
    i=0
    probs=[]
    Nvar = len(list(all_variations))
    for i,var in enumerate(all_variations):
        if i==winner:
            probs.append([var,1-pval*(Nvar-1)/Nvar])
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
    
    return Choice.objects.create(variation=variation, student=student)

def PlotResults(predictor,course_id):

    crs = Course.objects.get(pk=course_id)

    all_variations = crs.variation_set.all()

    data = DataPool(series=[{'options': {'source':Result.objects.filter(choice__variation=var).filter(choice__variation__course=crs)},'terms': ['choice__student__'+predictor, 'score']}for var in all_variations]) 
    
    plot = Chart(datasource=data,series_options=[
        {'options': {'type':'line'},
        'terms': {'choice__student__'+predictor: ['score' for i in range(len(all_variations))]}}])

    return plot         
        