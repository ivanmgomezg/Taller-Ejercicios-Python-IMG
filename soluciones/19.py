# ==================================================================================
# Ejercicio 19
# ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")

# Sin limpiar, contamos los que NO tienen formato YYYY-MM-DD
formato_valido = df['fecha_nacimiento'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False).sum()
formato_diferente = len(df) - formato_valido

print(f"Registros con formato diferente a YYYY-MM-DD: {formato_diferente}")