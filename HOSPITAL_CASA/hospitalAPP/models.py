from tabnanny import verbose
from django.db import models


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=20)
    nombre = models.CharField(max_length=60) 
    apellido = models.CharField(max_length=60)
    generos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    genero = models.CharField(max_length=1, choices=generos, default='F')
    telefono = models.CharField(max_length=15)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=15)
    password = models.CharField(max_length=130)

    def __str__(self):
     txt = "{0} {1} "
     return txt.format(self.id_paciente, self.nombre)

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    id_paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    parentesco=models.CharField(max_length=15) 
    correo = models.CharField(max_length=80)
    password = models.CharField(max_length=130)

    def __str__(self):
     txt = "{0} {1} "
     return txt.format(self.id_familiar, self.nombre)


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    especialidades = [
        ('1','Medico gral'),
        ('2', 'Cardiología'),
        ('3', 'Gastroenterología'),
        ('4', 'Neurología'),
        ('5', 'Nutriología'),
        ('6', 'Pediatría'),
        ('7', 'Psiquiatría'),
        ('8', 'Psicologia')
    ]
    especialidad = models.CharField(max_length=1, choices=especialidades, default='medico gral')
    registro = models.CharField(max_length=15)
    password = models.CharField(max_length=130)

    def __str__(self):
     txt = "{0} {1} "
     return txt.format(self.id_medico, self.nombre)

class Auxiliar(models.Model):
    id_auxiliar = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=130)

    def __str__(self):
     txt = "{0} {1} "
     return txt.format(self.id_auxiliar, self.nombre)

class Historia_clinica(models.Model):
    id_historia = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=300)
    id_paciente = models.ForeignKey(
        Paciente, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        txt = "{0} {1} "
        return txt.format(self.id_historia, self.diagnostico)

class Sugerencia(models.Model):
    id_sug = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    id_historia = models.ForeignKey(
        Historia_clinica, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
     txt = "{0} {1} "
     return txt.format(self.id_sug, self.descripcion)

class Signos_vitales(models.Model):
    id_signos = models.AutoField(primary_key=True)
    oximetria = models.DecimalField(max_digits=10, decimal_places=2)
    f_respiratoria = models.DecimalField(max_digits=10, decimal_places=2)
    f_cardiaca = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    p_arterial = models.DecimalField(max_digits=10, decimal_places=2)
    glicemias = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    id_paciente = models.ForeignKey(
        Paciente, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
     txt = "{0} {1} {2} {3} {4} {5} {6} {7}"
     return txt.format(self.id_signos, self.oximetria, self.f_respiratoria, self.f_cardiaca, self.temperatura, self.p_arterial, self.glicemias, self.fecha_hora, self.id_paciente,)

class Asignacion(models.Model):
    id_signos = models.AutoField(primary_key=True)
    id_historia = models.OneToOneField(
        Historia_clinica, null=False, blank=False, on_delete=models.CASCADE)
    id_medico = models.OneToOneField(
        Medico, null=False, blank=False, on_delete=models.CASCADE)
    id_familiar = models.OneToOneField(
        Familiar, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
     txt = "{0} {1} {2} "
     return txt.format(self.id_historia, self.id_medico, self.id_familiar)


class Comments(models.Model):

    class Meta:
        verbose_name = "Comment"
