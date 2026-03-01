# ==================================================================================
# Ejercicio 03
# Descripción: ¿Cuántas veces aparece el nombre "Juan" en el dataset?
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

# Nombre que queremos buscar en el dataset
nom_buscar = "Juan" 

# Contamos cuantas veces aparece "Juan" en la columna "nombre_cifrado"
contar = (df["nombre_cifrado"]==nom_buscar).sum() 

print(f"El nombre '{nom_buscar}' aparece {contar} veces en el dataset")