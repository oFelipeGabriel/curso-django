"""eventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inscricao.views import agora_view
from inscricao.views import cursos_list
from inscricao.views import AgoraView
from inscricao.views import CursoListView
from inscricao.views import CursoDetailView
from inscricao.views import CursoForm
from inscricao.views import CursoCreate2
from inscricao.views import recebe_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agora/', agora_view),
    path('cursos/', cursos_list),
    path('agora_now/', AgoraView.as_view(), name="agora_now"),
    path('cursos_list', CursoListView.as_view(), name="cursos_list"),
    path('curso_detail/<int:pk>', CursoDetailView.as_view(), name='curso_detail'),
    path('cursos_form/', CursoForm.as_view(), name="cursos_form"),
    path('cursos_form2/', CursoCreate2.as_view(), name="cursos_form2"),
    path('recebe_form/', recebe_form, name="cursos_form_recebe"),
    
]
