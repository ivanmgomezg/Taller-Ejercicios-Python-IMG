# ==================================================================================
# Ejercicio 21
# ¿Cuántas personas nacieron antes de 1960? 
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


lim = 1960

# Realizo el conteo de las personas que nacieron antes de 1960
conteo = (df_clean['anio_nacimiento'] < lim).sum()

print(f"Hay {conteo} personas que nacieron antes de 1960")   