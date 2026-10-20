from peewee import Model, AutoField, CharField, BooleanField
from datos.conexion import base_datos

class Comuna(Model):
    id_comuna = AutoField(primary_key=True)
    codigo_comuna = CharField(max_length=10, null=True)  
    nombre_comuna = CharField(max_length=100)
    habilitado = BooleanField(default=True)

    class Meta:
        database = base_datos
        table_name = 'comunas'