from django.shortcuts import render
from django.views import View
from django.views.generic.edit import BaseCreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from inscricao.models import Curso
from django import forms
from django.urls import reverse
from django.urls import reverse_lazy


# Create your views here.
def agora_view(request):
    now = datetime.now()
    print(request.META)
    html = "<html><body>Agora - %s.</body></html>" % now
    return HttpResponse(html)

def cursos_list(request):
    cursos = Curso.objects.all()

    option_template = "<li>{0}</li>"
    option_template = list(map(option_template.format, cursos))

    select_options = " ".join([item for item in option_template])
     
    html = f"<html><body><ul>{select_options}</ul></body></html>"
    return HttpResponse(html)

class AgoraView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        html = "<html><body>Agora = %s.</body></html>"% now
        return HttpResponse(html)


class CursoListView(ListView):
    model = Curso


class CursoDetailView(DetailView):
    model = Curso

class CursoForm(FormView):
    model = Curso
    template_name = "inscricao/curso_form.html"
    def is_valid(self):
        print('validado')

class CursoCreate(CreateView):
    model = Curso
    template_name = "inscricao/curso_form.html"

    def __init__(self, fields):
        self. fields = fields

class CursoCreate2(CreateView):
    #form_class = CursoForm
    model = Curso
    template_name = 'inscricao/curso_form.html'
    success_url = reverse_lazy('cursos_list')
    obj = None
    fields = '__all__'    

    #def form_invalid(self, form):
    #    return HttpResponse(" form is invalid.. this is just an HttpResponse object")

def recebe_form(request):
    
    print(request.POST['nome'])
    request_context = RequestContext(request)
    print(request_context)
    return CursoCreate(request.POST[1:])