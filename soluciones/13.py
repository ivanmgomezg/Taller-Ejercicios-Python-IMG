# ==================================================================================
# Ejercicio 13
# ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
contar = df["salario"].str.contains("[^0-9]").sum()
print("Número de registros con caracteres no numéricos en el campo salario:", contar)

