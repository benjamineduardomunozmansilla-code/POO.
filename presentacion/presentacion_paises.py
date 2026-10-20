from prettytable import PrettyTable
from datos.repositorio.repositorio_paises import listado_paises, guardar_pais
from datos.modelos.pais import Pais
from datos.auxiliar import pausar

def mostrar_paises():
    paises = listado_paises()
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre del País', 'Estado']
    
    print("\n" + "="*40)
    print("  LISTADO OFICIAL DE PAÍSES  ")
    print("="*40)
    
    if paises:
        for p in paises:
            estado = "Habilitado" if getattr(p, 'habilitado', True) else "Deshabilitado"
            tabla.add_row([p.id_pais, p.pais, p.habilitado])
        print(tabla)
    else:
        print("" \
        "No hay países registrados en la base de datos.")
    pausar()

def crear_pais_ui():
    print("\n" + "="*40)
    print("  REGISTRAR NUEVO PAÍS  ")
    print("="*40)
    nombre = input("Ingrese el nombre del nuevo País: ").strip()
    iso2 = input("ingrese el iso2").strip()
    iso3 = input("ingrese el iso3").strip()
    nacionalidad= input("ingrese nacionalidad").strip()

    if nombre:
        nuevo = Pais()
        nuevo.pais = nombre
        nuevo.iso2 = iso2
        nuevo.iso3 = iso3
        nuevo.nacionalidad = nacionalidad
        nuevo.habilitado = True
        
        if guardar_pais(nuevo):
            print(f"\n¡ÉXITO! El país '{nombre}' fue guardado y creado .")
        else:
            print("\n No se pudo guardar el país en la base de datos.")
    else:
        print(" El nombre del país no puede estar vacío.")
    pausar()