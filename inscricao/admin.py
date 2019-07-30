from django.contrib import admin
from inscricao.models import Participante


class ParticipanteAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Participante, ParticipanteAdmin)
