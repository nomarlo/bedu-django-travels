from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    GENRE = [("H", "Hombre"), ("M", "Mujer")]
    genre = models.CharField(max_length=1, choices=GENRE)
    key = models.CharField(max_length=40, null=True, blank=True)
    type = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Zone(models.Model):
    """ Define la tabla Zona """
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Tour(models.Model):
    """ Define la tabla Tour """
    name = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operator = models.CharField(max_length=45, null=True, blank=True)
    type = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.name)


class Salida(models.Model):
    """ Define la tabla Salida """
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    asientos = models.PositiveSmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tour = models.ForeignKey(Tour, related_name="salidas", on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}, {})".format(self.tour, self.fechaInicio, self.fechaFin)
