from dataclasses import fields
from rest_framework import serializers
from hospitalAPP.models import Asignacion, Auxiliar, Familiar, Historia_clinica, Medico, Paciente, Signos_vitales, Sugerencia

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__'


class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields='__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = '__all__'


class Historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_clinica
        fields = '__all__'


class Signos_vitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signos_vitales
        fields = '__all__'


class SugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugerencia
        fields = '__all__'


class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'
