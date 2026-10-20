import sys
from datos.auxiliar import (
    nombre_app, version_app, main_menu, 
    menu_comunas, menu_paises, menu_libros, limpiar_pantalla
)
from presentacion.presentacion_comunas import (
    mostrar_comunas, buscar_comuna_ui, datos_comuna, eliminar_comuna_ui
)
from presentacion.presentacion_paises import mostrar_paises, crear_pais_ui
from presentacion.presentacion_libros import (
    mostrar_libros, buscar_libro_ui, crear_libro_ui, eliminar_libro_ui
)

def encabezado(subtitulo=""):
    limpiar_pantalla()
    ancho = 54
    print("╔" + "═" * (ancho - 2) + "╗")
    print(f"║{nombre_app.center(ancho - 2)}║")
    print(f"║{version_app.center(ancho - 2)}║")
    if subtitulo:
        print("╠" + "═" * (ancho - 2) + "╣")
        print(f"║{subtitulo.center(ancho - 2)}║")
    print("╚" + "═" * (ancho - 2) + "╝\n")

def menu_gestion_comunas():
    while True:
        encabezado("MÓDULO: GESTIÓN DE COMUNAS")
        for k, v in menu_comunas.items():
            print(f"  [{k}] {v}")
        print()
        opcion = input("Seleccione una opción [1-5]: ").strip()
        
        if opcion == '1':
            mostrar_comunas()
        elif opcion == '2':
            buscar_comuna_ui()
        elif opcion == '3':
            datos_comuna()
        elif opcion == '4':
            eliminar_comuna_ui()
        elif opcion == '5':
            break

def menu_gestion_paises():
    while True:
        encabezado("MÓDULO: GESTIÓN DE PAÍSES")
        for k, v in menu_paises.items():
            print(f"  [{k}] {v}")
        print()
        opcion = input("Seleccione una opción [1-3]: ").strip()
        
        if opcion == '1':
            mostrar_paises()
        elif opcion == '2':
            crear_pais_ui()
        elif opcion == '3':
            break

def menu_gestion_libros():
    while True:
        encabezado("MÓDULO: GESTIÓN DE LIBROS")
        for k, v in menu_libros.items():
            print(f"  [{k}] {v}")
        print()
        opcion = input("Seleccione una opción [1-5]: ").strip()
        
        if opcion == '1':
            mostrar_libros()
        elif opcion == '2':
            buscar_libro_ui()
        elif opcion == '3':
            crear_libro_ui()
        elif opcion == '4':
            eliminar_libro_ui()
        elif opcion == '5':
            break

def menu_principal():
    while True:
        encabezado("MENÚ PRINCIPAL DE NAVEGACIÓN")
        for k, v in main_menu.items():
            print(f"  [{k}] {v}")
        print()
        opcion = input("Seleccione una opción [1-4]: ").strip()
        
        if opcion == '1':
            menu_gestion_comunas()
        elif opcion == '2':
            menu_gestion_paises()
        elif opcion == '3':
            menu_gestion_libros()
        elif opcion == '4':
            limpiar_pantalla()
            print("\n" + "="*45)
            print("    ¡Gracias por utilizar el sistema!    ")
            print("="*45 + "\n")
            sys.exit()

if __name__ == "__main__":
    menu_principal()