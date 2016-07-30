from service.models import *
from service.engine import *
import datetime

c = Course.objects.create(title="asdf")
v1 = Variation.objects.create(course=c,description="1")
v2 = Variation.objects.create(course=c,description="2")
s = Student.objects.create(name="asdf",birthday="1901-01-01",gender="male",originLanguageCode="en")
t = Test.objects.create(course=c,content="asdf")
for i in range(10):
    Choice.objects.create(variation=v1,student=s)
for i in range(10):
    Choice.objects.create(variation=v2,student=s)
for ch in Choice.objects.filter(variation=v1):
    Result.objects.create(test=t,choice=ch,score=10)
for ch in Choice.objects.filter(variation=v2):
    Result.objects.create(test=t,choice=ch,score=20)
tmp = chooseVariations(c,s)
