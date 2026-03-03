# ==================================================================================
# Ejercicio 18
# ¿Cuántos registros tienen `activo` como falso después de normalizar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántos registros tienen 'activo' como falso
registros = df_clean[df_clean["activo"] == False].shape[0]
print(f"El número de registros con 'activo' como falso después de normalizar es: {registros}")