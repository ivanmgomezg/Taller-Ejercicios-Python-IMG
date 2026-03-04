# ==================================================================================
# Ejercicio 27
# ¿Cuál es la ciudad con más "Ingenieros"?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
profesion = "Ingeniero"

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, profesion=profesion)

# Contamos el número de ingenieros por ciudad
conteo_ciudades = df_filtrado['ciudad'].value_counts()

# Encontramos la ciudad con más ingenieros
ciudad_max_ingenieros = conteo_ciudades.idxmax()
cantidad_ingenieros = conteo_ciudades.max()

print(f"La ciudad con más ingenieros es '{ciudad_max_ingenieros}' con {cantidad_ingenieros} ingenieros.")