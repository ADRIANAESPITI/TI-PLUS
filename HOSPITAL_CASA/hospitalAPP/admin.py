from django.contrib import admin

from hospitalApp.models import Asignacion, Auxiliar, Familiar, Historia_clinica, Medico, Paciente, Signos_vitales, Sugerencia

admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Medico)
admin.site.register(Auxiliar)
admin.site.register(Historia_clinica)
admin.site.register(Sugerencia)
admin.site.register(Signos_vitales)
admin.site.register(Asignacion)

