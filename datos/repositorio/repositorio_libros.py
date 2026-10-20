from datos.modelos.libro import Libro
from datos.conexion import base_datos

def listado_libros():
    """Obtiene todos los libros habilitados desde la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Libro], safe=True)
        return list(Libro.select().where(Libro.habilitado == True))
    except Exception as e:
        print(f"Error al listar libros: {e}")
        return []

def guardar_libro(libro):
    """Guarda un nuevo libro directamente en la base de datos."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Libro], safe=True)
        libro.save()
        return True
    except Exception as e:
        print(f"Error al guardar libro: {e}")
        return False

def buscar_libro_por_titulo(titulo):
    """Busca libros por coincidencia en el título."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Libro], safe=True)
        return list(Libro.select().where(
            (Libro.titulo.contains(titulo)) & (Libro.habilitado == True)
        ))
    except Exception as e:
        print(f"Error al buscar libro: {e}")
        return []

def eliminar_libro_por_id(id_libro):
    """Realiza la baja lógica de un libro por su ID."""
    try:
        if base_datos.is_closed():
            base_datos.connect()
        base_datos.create_tables([Libro], safe=True)
        libro = Libro.get_by_id(id_libro)
        libro.habilitado = False
        libro.save()
        return True
    except Exception as e:
        print(f"Error al eliminar libro: {e}")
        return False