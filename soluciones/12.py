# ==================================================================================
# Ejercicio 11
# ¿Cuántos registros tienen el campo email con espacios adicionales?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
contar = df
print("Número de registros con espacios adicionales en el campo email:", contar[contar["email"].str.contains(" ")].shape[0])