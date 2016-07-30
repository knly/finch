from service.models import *
from service.engine import *
import datetime
import random

c = Course.objects.create(title="asdf")
v1 = Variation.objects.create(course=c,description="1")
v2 = Variation.objects.create(course=c,description="2")
s1 = Student.objects.create(name="asdf",birthday="1901-01-01",gender="male",originLanguageCode="en")
s2 = Student.objects.create(name="asdfea",birthday="1902-02-02",gender="female",originLanguageCode="en")
t = Test.objects.create(course=c,content="asdf")
for i in range(10):
    Choice.objects.create(variation=v1,student=random.choice([s1,s2]))
for i in range(10):
    Choice.objects.create(variation=v2,student=random.choice([s1,s2]))
for ch in Choice.objects.filter(variation=v1):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
for ch in Choice.objects.filter(variation=v2):
    Result.objects.create(test=t,choice=ch,score=15+10*random.random())
p1 = 0
p2 = 0
s3 = Student.objects.create(name="asdfb",birthday="1903-03-03",gender="male",originLanguageCode="en")
for i in range(100):
    tmp = chooseVariations(c,s3)
    if tmp.variation == v1:
        p1+=1
    if tmp.variation == v2:
        p2+=1
print(p1/(p1+p2))
print(p2/(p1+p2))
