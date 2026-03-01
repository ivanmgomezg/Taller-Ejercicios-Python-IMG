# ==================================================================================
# Ejercicio 04
# Descripción: ¿Cuál es el nombre más frecuente y cuántas veces aparece?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.transformaciones as transf

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------

# Decodificamos la columna "nombre_cifrado" usando ROT13 para obtener los nombres reales 
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: transf.rot13(x)) 

# Contamos la frecuencia de cada nombre en la columna "nombre_cifrado"
conteo = df["nombre_cifrado"].value_counts() 

# Obtenemos el nombre más frecuente utilizando idxmax() que devuelve el índice del valor máximo en la serie de conteo
nombre_mas_frecuente = conteo.idxmax() 

# Obtenemos la frecuencia del nombre más frecuente utilizando max() que devuelve el valor máximo en la serie de conteo
frecuencia = conteo.max() 

print(f"El nombre más frecuente es '{nombre_mas_frecuente}' y aparece {frecuencia} veces en el dataset") 