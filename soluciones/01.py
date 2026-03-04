# ==================================================================================
# Ejercicio 01
# Descripción: ¿Cuántas filas tienen el campo id con caracteres no numéricos?
# ==================================================================================

# manejo de rutas y configuración del entorno de ejecución
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión desde la carpeta utils para cargar los datos
import utils.conexion as conexion 

# -------------------------------------------------------

df = conexion.cargar_datos_csv("personas.csv") # Cargamos el CSV en un DataFrame para poder manipularlo

id_no_num = (~df["id"].str.isnumeric()).sum() #En esta variable almaceno la cantidad de id que no(~) son numericos

print(f"De las 300.000 filas hay {id_no_num} filas con id que contienen caracteres no numéricos")