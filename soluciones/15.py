# ==================================================================================
# Ejercicio 15
# ¿Cuál es el salario máximo después de limpiar? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

maximo = df_clean["salario"].max()
print(f"El salario máximo después de limpiar es: {maximo:,.2f}")