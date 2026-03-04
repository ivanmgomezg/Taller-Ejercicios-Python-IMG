# ==================================================================================
# Ejercicio 02
# Descripción: ¿Cuántas veces aparece el nombre "Maria" en el dataset?
# ==================================================================================

# manejo de rutas y configuración del entorno de ejecución
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.limpieza as limp

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------

#Decodificamos la columna "nombre_cifrado" usando ROT13 para obtener los nombres reales 
df["nombre_cifrado"] = df["nombre_cifrado"].apply(limp.rot13)

# Nombre que queremos buscar en el dataset
nom_buscar = "Maria" 

# Contamos cuantas veces aparece "Maria" en la columna "nombre_cifrado"
contar = (df["nombre_cifrado"]==nom_buscar).sum() 

print(f"El nombre '{nom_buscar}' aparece {contar} veces en el dataset")