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

    pred = Student._meta.get_field(predictor)
    crs = Course.objects.get(pk=course_id)

    all_variations = crs.variation_set.all()
    relevant_results = Result.objects.filter(choice__variation__course=crs)

    """
    # Deduce possible predictors
    pred = Student._meta.get_field(predictor)
    possible_predictors=[]
    for r in relevant_results:
        for p in possible_predictors:
            if r.student.pred!=p:
                possible_predictors.append(r.student.pred)

    print(possible_predictors)

    datapoints=[]
    for p in possible_predictors:
        dummy = Student.objects.create(pred=p)
        dumtest = Test.objects.create(course=crs)
        for var in all_variations:
            average = 0
            dumchoice = Choice.objects.create(student=dummy,variation=var)
            N = len(relevant_results.filter(choice__student__pred=p)).filter(choice__variation=var)
            for r in relevant_results.filter(pred=p):
                average += r.score / N
            avres = Result.object.create(test=dumtest,choice=dumchoice,score=average)
            datapoints.append(avres)
            dummy.delete()
            dumtest.delete()
            dumchoice.delete()
            avres.delete()

    idlist = []
    for res in datapoints:
        idlist.append(res.id)

    datares = Result.objects.filter(id__in=idlist)

   # data = DataPool(series=[
    #    {'options': 
     #       {'source':Result.objects.filter(choice__variation=var).filter(choice__variation__course=crs)},
      #          'terms': termlist} for var in all_variations])
    """
    data = DataPool(series=[{'options':
        {'source':relevant_results.filter(choice__variation=var)},
            'terms':['choice__student__'+predictor,'score']} for var in all_variations])

    plot = Chart(datasource=data,series_options=[
        {'options': {'type':'line'},
        'terms': {'choice__student__'+predictor: ['score']}}])

    return plot
