from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^mine/$', views.ManageCourseListView.as_view(), name='manage_course_list'),
    url(r')
]