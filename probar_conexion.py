from datos.conexion import base_datos

print("Verificando conexión con la base de datos...")

try:
    # Comprobamos el estado de la conexión 
    if base_datos.is_closed():
        base_datos.connect()
    
    print("Conexión exitosa a la base de datos ")
    
    # Cerramos la conexión de forma limpia
    base_datos.close()

except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
