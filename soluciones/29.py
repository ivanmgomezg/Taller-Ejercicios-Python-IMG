# ==================================================================================
# Ejercicio 29
# ¿Cuántos registros tienen email con dominio "gmail.com"?
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

# Filtramos los registros con email que termina en "gmail.com"
filtro_gmail = df_clean['email'].str.endswith('@gmail.com', na=False)
registros_gmail = df_clean[filtro_gmail]

# Contamos el número de registros con email de gmail
cantidad_gmail = len(registros_gmail)

print(f"El número de registros con email de gmail es: {cantidad_gmail}")