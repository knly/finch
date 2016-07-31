from service.models import *
from service.engine import *
import datetime
import random

c = Course.objects.create(title="What do people laugh about?")
v1 = Variation.objects.create(course=c,description="gravity")
l1 = Lesson.objects.create(variation=v1,index=1,content="![gravity](https://img.buzzfeed.com/buzzfeed-static/static/2016-04/6/9/enhanced/webdr08/enhanced-11396-1459948994-2.jpg?no-auto)")
v2 = Variation.objects.create(course=c,description="argon")
l2 = Lesson.objects.create(variation=v2,index=2,content="![argon](https://img.buzzfeed.com/buzzfeed-static/static/2016-04/6/10/enhanced/webdr09/enhanced-15891-1459953109-5.jpg)")
v3 = Variation.objects.create(course=c,description="higgs")
l3 = Lesson.objects.create(variation=v3,index=3,content="![higgs](https://img.buzzfeed.com/buzzfeed-static/static/2015-04/20/16/enhanced/webdr02/enhanced-425-1429562245-10.jpg)")
v4 = Variation.objects.create(course=c,description="photon")
l4 = Lesson.objects.create(variation=v4,index=4,content="![photon](https://img.buzzfeed.com/buzzfeed-static/static/2015-04/22/12/enhanced/webdr05/edit-6242-1429718545-18.jpg)")
v5 = Variation.objects.create(course=c,description="quark")
l5 = Lesson.objects.create(variation=v5,index=5,content="# What does a subatomic duck say? /n Quark!")
s1 = Student.objects.create(name="Bob",birthday="1990-07-15",gender="male",originLanguageCode="en")
s2 = Student.objects.create(name="Alice",birthday="1985-02-08",gender="female",originLanguageCode="en")
t = Test.objects.create(course=c,content="Did that joke make you laugh out loud? (Type 0 or 1)",correct_answer="1")
for i in range(10):
    Choice.objects.create(variation=v1,student=random.choice([s1,s2]),startingTime="2016-01-01")
for i in range(10):
    Choice.objects.create(variation=v2,student=random.choice([s1,s2]),startingTime="2016-01-01")
for i in range(10):
    Choice.objects.create(variation=v3,student=random.choice([s1,s2]),startingTime="2016-01-01")
for i in range(10):
    Choice.objects.create(variation=v4,student=random.choice([s1,s2]),startingTime="2016-01-01")
for i in range(10):
    Choice.objects.create(variation=v5,student=random.choice([s1,s2]),startingTime="2016-01-01")
for ch in Choice.objects.filter(variation=v1):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
for ch in Choice.objects.filter(variation=v2):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
for ch in Choice.objects.filter(variation=v3):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
for ch in Choice.objects.filter(variation=v4):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
for ch in Choice.objects.filter(variation=v5):
    Result.objects.create(test=t,choice=ch,score=10+10*random.random())
p1=0
p2=0
p3=0
p4=0
p5=0
s3 = Student.objects.create(name="William",birthday="1989-10-25",gender="male",originLanguageCode="en")
for i in range(100):
    tmp = chooseVariations(c,s3)
    if tmp.variation == v1:
        p1+=1
    if tmp.variation == v2:
        p2+=1
    if tmp.variation == v3:
        p3+=1
    if tmp.variation == v4:
        p4+=1
    if tmp.variation == v5:
        p5+=1
print(p1/(p1+p2+p3+p4+p5))
print(p2/(p1+p2+p3+p4+p5))
print(p3/(p1+p2+p3+p4+p5))
print(p4/(p1+p2+p3+p4+p5))
print(p5/(p1+p2+p3+p4+p5))
