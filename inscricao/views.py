from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import HttpResponse
from datetime import datetime
from inscricao.models import Curso


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