from django.views.generic.list import ListView
from freecod.models import Freecode
from django.shortcuts import render
from django.http import HttpResponse


class  FreecodeListView(ListView):
    model = Freecode
    template_name = 'freecode.html' 
    context_object_name = 'freecode'
    queryset = Freecode.objects.all()[:3]
    #paginate_by = 1


def freecode_view (request,*args, **kwargs):
    return HttpResponse("heyadamim bu bir deneme !!!")



