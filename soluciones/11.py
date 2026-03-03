# ==================================================================================
# Ejercicio 11
# ¿Cuántas profesiones únicas existen después de normalizar?
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

# Contamos cuántas profesiones únicas existen en la columna "profesion" después de normalizar
profesiones_unicas = df_clean["profesion"].nunique()  
print(f"El número de profesiones únicas después de normalizar es: {profesiones_unicas}")