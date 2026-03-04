# ==================================================================================
# Ejercicio 30
# ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? 
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

nombre = "Jose"
apellido = "Garcia"

df_filtro = filt.filtrar(df_clean, nombre_cifrado=nombre, apellido_cifrado=apellido)
contar = len(df_filtro)

print(f"El número de registros con nombre {nombre} y apellido {apellido} es: {contar}")

