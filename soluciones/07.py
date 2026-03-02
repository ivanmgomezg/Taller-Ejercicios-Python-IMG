# ==================================================================================
# Ejercicio 07
# ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion   

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función limpiar_dataset del módulo de limpieza

# Contamos cuántos registros tienen la ciudad "Medellin" en la columna "ciudad"
ciudad = 'medellin'
conteo_ciudad = df_clean[df_clean["ciudad"] == ciudad].shape[0]

print(f"El número de registros con la ciudad '{ciudad.capitalize()}' es: {conteo_ciudad}")
