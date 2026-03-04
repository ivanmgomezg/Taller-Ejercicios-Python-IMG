# ==================================================================================
# Ejercicio 22
# ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
from datetime import datetime

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

# Calculamos la edad de cada persona
fecha_actual = datetime(2026, 2, 26)

#nueva columna edad con el calculo de la edad a partir de la fecha de nacimiento
df_clean['edad'] = (fecha_actual - df_clean['fecha_nacimiento']).dt.days // 365

# Contamos cuántas personas tienen más de 50 años
personas_mayores_50 = df_clean[df_clean['edad'] > 50].shape[0]
print(f"El número de personas con más de 50 años es: {personas_mayores_50}")    
