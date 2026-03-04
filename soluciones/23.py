# ==================================================================================
# Ejercicio 23
# ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? 
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
nombre_cifrado = "Carlos"
ciudad = "Cali"

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, nombre_cifrado=nombre_cifrado, ciudad=ciudad)

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con nombre 'Carlos' y ciudad 'Cali': {cantidad_registros}")