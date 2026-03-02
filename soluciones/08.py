# ==================================================================================
# Ejercicio 08
# ¿Cuántas ciudades únicas existen después de normalizar? 
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

# Contamos cuántas ciudades únicas existen en la columna "ciudad" después de normalizar
ciudades_unicas = df_clean["ciudad"].nunique()  
print(f"El número de ciudades únicas después de normalizar es: {ciudades_unicas}")