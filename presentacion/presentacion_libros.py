from prettytable import PrettyTable
from datos.repositorio.repositorio_libros import (
    listado_libros, guardar_libro, buscar_libro_por_titulo, eliminar_libro_por_id
)
from datos.modelos.libro import Libro
from datos.auxiliar import pausar

def mostrar_libros():
    libros = listado_libros()
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'ISBN', 'Título', 'Autor', 'Estado']
    
    print("\n" + "="*50)
    print("        LISTADO OFICIAL DE LIBROS       ")
    print("="*50)
    
    if libros:
        for l in libros:
            estado = "Disponible" if getattr(l, 'habilitado', True) else "No disponible"
            tabla.add_row([l.id_libro, l.isbn or 'S/N', l.titulo, l.autor, estado])
        print(tabla)
    else:
        print(" No hay libros registrados en la base de datos.")
    pausar()

def buscar_libro_ui():
    print("\n" + "="*50)
    print("          BUSCAR LIBRO POR TÍTULO       ")
    print("="*50)
    titulo = input("Ingrese el título o parte del título a buscar: ").strip()
    
    if titulo:
        resultados = buscar_libro_por_titulo(titulo)
        tabla = PrettyTable()
        tabla.field_names = ['ID', 'ISBN', 'Título', 'Autor']
        if resultados:
            for l in resultados:
                tabla.add_row([l.id_libro, l.isbn or 'S/N', l.titulo, l.autor])
            print(tabla)
        else:
            print(f" No se encontraron libros con el título '{titulo}'.")
    else:
        print(" El título no puede estar vacío.")
    pausar()

def crear_libro_ui():
    print("\n" + "="*50)
    print("          REGISTRAR NUEVO LIBRO         ")
    print("="*50)
    isbn = input("Ingrese el ISBN del libro (opcional): ").strip()
    titulo = input("Ingrese el Título del libro: ").strip()
    autor = input("Ingrese el Autor del libro: ").strip()
    
    if titulo and autor:
        nuevo = Libro()
        nuevo.isbn = isbn if isbn else 'Sin ISBN'
        nuevo.titulo = titulo
        nuevo.autor = autor
        nuevo.habilitado = True
        
        if guardar_libro(nuevo):
            print(f"\n ¡ÉXITO! El libro '{titulo}' fue registrado y guardado en phpMyAdmin.")
        else:
            print("\n No se pudo guardar el libro en la base de datos.")
    else:
        print(" El Título y el Autor son campos obligatorios.")
    pausar()

def eliminar_libro_ui():
    print("\n" + "="*50)
    print("            ELIMINAR LIBRO              ")
    print("="*50)
    try:
        id_libro = int(input("Ingrese el ID del libro que desea eliminar: "))
        confirmar = input(f"¿Está seguro de eliminar el libro ID {id_libro}? (s/n): ").lower()
        if confirmar == 's':
            if eliminar_libro_por_id(id_libro):
                print(" Libro deshabilitado/eliminado correctamente.")
            else:
                print("No se encontró el libro especificado.")
    except ValueError:
        print(" Debe ingresar un número de ID válido.")
    pausar()