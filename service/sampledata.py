from service.models import *
from service.engine import *
import datetime
import random
import markdown

c = Course.objects.create(title="Quantum Mechanics", description="Understanding the foundations of modern physics.")
content1 = markdown.markdown("# Lesson 1 \n\n Let's learn using a **simple derivation** of the equation. \n\n [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/IsX5iUKNT2k/0.jpg)](http://www.youtube.com/watch?v=IsX5iUKNT2k)", safe_mode=True)
content2 = markdown.markdown("# Lesson 1 \n\n Let's learn through understanding the **concepts** of the equation. \n\n[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/aU_bd7fku90/0.jpg)](http://www.youtube.com/watch?v=aU_bd7fku90)", safe_mode=True)
test_content = markdown.markdown("Why don't we experience the wave nature of matter on our everyday lives? \n\n \n\n a) The particles are connected in a complex system which suppresses the effect. \n\n b) It is not yet clear to science. \n\n c) The wavelength is to small for our scales.", safe_mode=True)
t = Test.objects.create(course=c,content=test_content, correct_answer="c")
v1 = Variation.objects.create(course=c,description="Derivation")
l1 = Lesson.objects.create(variation=v1, index=0, content=content1)
v2 = Variation.objects.create(course=c,description="Conceptual")
l2 = Lesson.objects.create(variation=v2, index=0, content=content2)
variations = [v1, v2]
genders = ["male", "female"]
language_codes = ["en", "iw", "de"]
names = ["Lagrange", "Dirac", "Tesla", "Bohr", "Feynman",
         "Planck", "Hopper", "Born", "Heisenberg", "Einstein",
         "Zwicky", "Curie", "Euler", "Hamilton", "Cantor",
         "Lie", "Newton", "Kepler", "Lorentz", "Halmholz"]
for i in range(20):
    name = "SE_student" + i.__str__()
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
                          score=30+random.randrange(30),
                          finished_course=finished_course)