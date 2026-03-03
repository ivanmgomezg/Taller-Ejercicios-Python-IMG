# ==================================================================================
# Ejercicio 20
# ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Dejo en fecha de nacimiento solo el año para facilitar la comparación
df_clean['anio_nacimiento'] = df_clean['fecha_nacimiento'].dt.year

lim_inf = 1990
lim_sup = 2000

conteo = df_clean['anio_nacimiento'].between(lim_inf, lim_sup).sum()

print(f"Personas nacidas entre {lim_inf} y {lim_sup}: {conteo}")

