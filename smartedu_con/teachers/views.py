from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher




class  TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html' 
    context_object_name = 'teachers'
    queryset = Teacher.objects.all()[:3]
    #paginate_by = 1


    #def get_queryset(self):
        #return Teacher.objects.all()[:3]

class TeacherDetailView(DetailView):
    model = Teacher
    tepmlate_name = 'teacher.html'



