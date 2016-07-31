from service.models import *
from service.engine import *
import datetime
import random

c = Course.objects.create(title="Schrodinger Equation")
t = Test.objects.create(course=c,content="Isn't Schrodinger Equation great?", correct_answer="yes")
v1 = Variation.objects.create(course=c,description="Derivation")
v2 = Variation.objects.create(course=c,description="Conceptual")
variations = [v1, v2]
genders = ["male", "female"]
language_codes = ["en", "iw", "de"]
for i in range(20):
    name = "student" + i.__str__()
    birthday = "199" + (i%10).__str__() + "-01-01"
    gender = genders[i%2]
    language_code = language_codes[i%3]
    s = Student.objects.create(name=name, birthday=birthday, gender=gender, originLanguageCode=language_code)
    variation = variations[(i//2) % 2]
    ch = Choice.objects.create(variation=variation,
                         student=s,
                         startingTime="2016-01-01")
    finished_course = True
    if (random.randrange(100) < 25):
        finished_course = False
    r = Result.objects.create(test=t,
                          choice=ch,
                          score=10+10*random.random(),
                          finished_course=finished_course)
"""
for i in range(100):
    tmp = chooseVariations(c,s3)
    if tmp.variation == v1:
        p1+=1
    if tmp.variation == v2:
        p2+=1
print(p1/(p1+p2))
print(p2/(p1+p2))
"""