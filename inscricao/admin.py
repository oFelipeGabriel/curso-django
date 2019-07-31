from django.contrib import admin
from inscricao.models import Participante
from inscricao.models import Curso
from inscricao.models import Matricula


class ParticipanteAdmin(admin.ModelAdmin):
    pass

class MatriculaeAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)
# Register your models here.
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Curso)
admin.site.register(Matricula, MatriculaeAdmin)
