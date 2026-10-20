from datos.modelos.pais import Pais
from datos.conexion import base_datos

def listado_paises():
    """Obtiene todos los países habilitados desde la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Pais], safe=True)
        return list(Pais.select().where(Pais.habilitado == True))
    except Exception as e:
        print(f"Error al listar países: {e}")
        return []

def guardar_pais(pais):
    """Guarda un nuevo país directamente en la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        # Asegura que la tabla exista antes de insertar
        base_datos.create_tables([Pais], safe=True)
        pais.save()
        return True
    except Exception as e:
        print(f"Error al guardar país: {e}")
        return False