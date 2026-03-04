# ==================================================================================
# Ejercicio 22
# ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
import pandas as pd
from datetime import datetime


# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

# Definimos la fecha de referencia
fecha_actual = datetime(2026, 2, 26)

# Cálculo de edad exacta
def calcular_edad(fecha_nac):
    if pd.isna(fecha_nac): return None
    # 1. Restamos los años
    edad = fecha_actual.year - fecha_nac.year
    # 2. Restamos 1 si no ha llegado su cumpleaños este año
    # Comparamos (mes, día) actual vs (mes, día) de nacimiento
    ha_cumplido_años = (fecha_actual.month, fecha_actual.day) >= (fecha_nac.month, fecha_nac.day)
    if not ha_cumplido_años:
        edad -= 1
    return edad

# Aplicamos la función a la columna
df_clean['edad'] = df_clean['fecha_nacimiento'].apply(calcular_edad)

# Contamos los mayores de 50
personas_mayores_50 = (df_clean['edad'] > 50).sum()

print(f"El número de personas con más de 50 años es: {personas_mayores_50}")
