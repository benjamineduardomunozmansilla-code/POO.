from peewee import Model, AutoField, CharField, BooleanField
from datos.conexion import base_datos

class Libro(Model):
    id_libro = AutoField(primary_key=True)
    isbn = CharField(max_length=20, null=True)
    titulo = CharField(max_length=150)
    autor = CharField(max_length=100)
    habilitado = BooleanField(default=True)

    class Meta:
        database = base_datos
        table_name = 'libro'