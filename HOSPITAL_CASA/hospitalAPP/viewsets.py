from rest_framework import viewsets
from . import models
from . import serializers

class PacienteViewset(viewsets.ModelViewSet):
    queryset=models.Paciente.objects.all()
    serializer_class=serializers.PacienteSerializer


class FamiliarViewset(viewsets.ModelViewSet):
    queryset=models.Familiar.objects.all()
    serializer_class=serializers.FamiliarSerializer


class MedicoViewset(viewsets.ModelViewSet):
    queryset=models.Medico.objects.all()
    serializer_class=serializers.MedicoSerializer


class AuxiliarViewset(viewsets.ModelViewSet):
    queryset=models.Auxiliar.objects.all()
    serializer_class=serializers.AuxiliarSerializer


class Historia_clinicaViewset(viewsets.ModelViewSet):
    queryset=models.Historia_clinica.objects.all()
    serializer_class=serializers.Historia_clinicaSerializer


class Signos_vitalesViewset(viewsets.ModelViewSet):
    queryset=models.Signos_vitales.objects.all()
    serializer_class=serializers.Signos_vitalesSerializer


class SugerenciaViewset(viewsets.ModelViewSet):
    queryset=models.Sugerencia.objects.all()
    serializer_class=serializers.SugerenciaSerializer


class AsignacionViewset(viewsets.ModelViewSet):
    queryset=models.Asignacion.objects.all()
    serializer_class=serializers.AsignacionSerializer