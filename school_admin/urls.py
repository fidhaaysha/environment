from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns=[
    path('login', views.login),
    path('teachers',views.viewteachers),
    path('students',views.viewstudents),
]