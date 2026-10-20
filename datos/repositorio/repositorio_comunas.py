from datos.modelos.comuna import Comuna
from datos.conexion import base_datos

def listado_comunas():
    """Obtiene todas las comunas habilitadas desde la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Comuna], safe=True)
        return list(Comuna.select().where(Comuna.habilitado == True))
    except Exception as e:
        print(f"Error al listar comunas: {e}")
        return []

def guardar_comuna(comunas):
    """Guarda una nueva comuna directamente en la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Comuna], safe=True)
        comunas.save()
        return True
    except Exception as e:
        print(f"Error al guardar comuna: {e}")
        return False

def comuna_por_nombre(nombre):
    """Busca comunas por nombre que estén habilitadas."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Comuna], safe=True)
        # Usamos .contains() en lugar de .ilike() para que funcione perfectamente en MySQL
        return list(Comuna.select().where(
            (Comuna.nombre_comuna.contains(nombre)) & (Comuna.habilitado == True)
        ))
    except Exception as e:
        print(f"Error al buscar comuna por nombre: {e}")
        return []

def eliminar_comuna_por_id(id_comuna):
    """Realiza la baja lógica de una comuna por su ID."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Comuna], safe=True)
        comuna = Comuna.get_by_id(id_comuna)
        comuna.habilitado = False
        comuna.save()
        return True
    except Exception as e:
        print(f"Error al eliminar comuna: {e}")
        return False