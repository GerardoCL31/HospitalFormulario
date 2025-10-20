from django.db import models

class Cita(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=9)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    medicacion = models.BooleanField(default=False)
    medicamento = models.CharField(max_length=100, blank=True, null=True)
    dosis_diaria = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.fecha_cita}"
