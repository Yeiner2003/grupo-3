from django.db import models 

class hospedaje (models.model):
    nombre = models.charfield(max_length=200)
    direccion = models. charfield(max_length = 100)
    correo = models.charfield()
    tipo_hospedaje = models. charfield()
    descripcion = models . charfield ()
    tarifa_base = models .charfield()
    
