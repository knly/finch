from django.contrib import admin
from .models import *
# TODO edit template of admin page


class LessonInline(admin.TabularInline):
    model = Lesson


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    inlines = [VariationInline]
admin.site.register(Course, CourseAdmin)


class VariationAdmin(admin.ModelAdmin):
    fields = ['description']
    inlines = [LessonInline]
    list_display = ('course', 'description')
admin.site.register(Variation, VariationAdmin)


admin.site.register(Test)
admin.site.register(Student)
admin.site.register(Choice)
admin.site.register(Result)
