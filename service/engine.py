from .models import *
import random
import scipy.stats
from datetime import date


def chooseVariations(course, student):
    all_variations = course.variation_set.all()
    # Perform chi-square test
    scores=[]
    avg_score=0
    find_unfinished_results(course)
    NTot = len(Result.objects.filter(choice__variation__course=course,finished_course=True))
    if NTot == 0:
        variation = random.choice(all_variations)
        return Choice.objects.create(variation=variation,student=student, startingTime=date.today())
    for i, var in enumerate(all_variations):
        student_list = Result.objects.filter(choice__variation=var, finished_course=True)
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

    return Choice.objects.create(variation=variation, student=student, startingTime=date.today())

def PlotResults(predictor,course_id):

    pred = Student._meta.get_field(predictor)
    crs = Course.objects.get(pk=course_id)

    # TODO verify that this is the only place where we access results
    print('000000000000000000000000')
    find_unfinished_results(crs)
    print('11111111111111111111111')

    all_variations = crs.variation_set.all()
    relevant_results = Result.objects.filter(choice__variation__course=crs)
    print(len(relevant_results))
    print('222222222222222222222222')
    # Deduce possible predictors
    possible_strpred=[]
    for r in relevant_results:
        if len(possible_strpred)==0:
            possible_strpred.append(str(getattr(r.choice.student,predictor)))
            print(possible_strpred)
        no_append=False
        for p in possible_strpred:
            if str(getattr(r.choice.student,predictor)) == p:
                no_append=True

        if(not no_append):
            possible_strpred.append(str(getattr(r.choice.student,predictor)))
        print(possible_strpred)
    print(len(possible_strpred))
    print('333333333333333333333333333333333')
    print()
    data_pack=[]
    varpack=[]
    for p in possible_strpred:
      #  print("p = " + p.__str__() + ", -------------------------------")
        datapoints=[]
        for var in all_variations:
            varpack.append(var.description)
       #     print("var = " + var.__str__() + "- - - - - - - - - - - - - - ")
            average = 0
            varlist = relevant_results.filter(choice__variation=var)
            N=0 # TODO raises bug when not all choices and predictors were tried
            for r in varlist:
                if getattr(r.choice.student,predictor) == p:
                    if r.finished_course:
                        average += r.score
                        N+=1
            if N != 0:
                average /= N
            datapoints.append(average)
        data_pack.append(datapoints)
    data_out = { 'possible_strpred':possible_strpred, 'data_pack':data_pack, 'vars': varpack }
    print('44444444444444444444444444444444444')
    return data_out


MAX_SESSION_TIME_DAYS = 7


def find_unfinished_results(course):
    for variation in course.variation_set.all():
        for choice in variation.choice_set.all():
            if not hasattr(choice, 'result'):
                if ((date.today() - choice.startingTime).days >= MAX_SESSION_TIME_DAYS):
                    result = Result.objects.create(choice=choice, score=-1, finished_course=False)
