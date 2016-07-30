from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^course/(?P<course_id>[0-9]+)/edit$', views.edit_course, name='edit_course'),
    url(r'^course/(?P<course_id>[0-9]+)/$', views.prepare_course, name='prepare_course'),
    url(r'^course/(?P<course_id>[0-9]+)/take/(?P<student_id>[0-9]+)$', views.take_course, name='take_course'),
]
