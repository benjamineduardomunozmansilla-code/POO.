from peewee import Model, AutoField, CharField, BooleanField
from datos.conexion import base_datos

class Pais(Model):
    id_pais = AutoField(primary_key=True)
    pais = CharField(max_length=100)
    nacionalidad =CharField(max_length=50)
    iso2=CharField(max_length=2)
    iso3=CharField(max_length=3)
    habilitado = BooleanField(default=True)

    class Meta:
        database = base_datos
        table_name = 'paises'