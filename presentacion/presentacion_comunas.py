from prettytable import PrettyTable
from negocio.negocio_comunas import cargar_comunas, buscar_comunas, crear_comuna
from datos.repositorio.repositorio_comunas import eliminar_comuna_por_id
from datos.auxiliar import pausar

def mostrar_comunas():
    tabla = PrettyTable()
    tabla = cargar_comunas(tabla)
    print("\n" + "="*40)
    print("   LISTADO OFICIAL DE COMUNAS   ")
    print("="*40)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print("No hay comunas registradas .")
    pausar()

def buscar_comuna_ui():
    print("\n" + "="*40)
    print("   BUSCAR COMUNA POR NOMBRE   ")
    print("="*40)
    nombre = input("Ingrese el nombre de la comuna : ").strip()
    if nombre:
        tabla = PrettyTable()
        tabla = buscar_comunas(tabla, nombre)
        if tabla.rowcount > 0:
            print(tabla)
        else:
            print(f" No se encontraron comunas que coincidan con '{nombre}'.")
    else:
        print(" El nombre no puede estar vacío.")
    pausar()

def datos_comuna():
    print("\n" + "="*40)
    print("  REGISTRAR NUEVA COMUNA  ")
    print("="*40)
    codigo = input("Ingrese el Código de la Comuna (ej: C01): ").strip()
    nombre = input("Ingrese el Nombre de la Comuna: ").strip()
    
    if codigo and nombre:
        crear_comuna(codigo, nombre)
    else:
        print(" Error: Todos los campos son obligatorios.")
    pausar()

def eliminar_comuna_ui():
    print("\n" + "="*40)
    print("  ELIMINAR COMUNA  ")
    print("="*40)
    try:
        id_comuna = int(input("Ingrese el ID de la comuna que desea eliminar: "))
        confirmar = input(f"¿Está seguro de eliminar la comuna ID {id_comuna}? (s/n): ").lower()
        if confirmar == 's':
            res = eliminar_comuna_por_id(id_comuna)
            if res:
                print("Comuna deshabilitada/eliminada correctamente.")
            else:
                print(" No se encontró la comuna especificada.")
    except ValueError:
        print("Debe ingresar un número de ID válido.")
    pausar()