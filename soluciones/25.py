# ==================================================================================
# Ejercicio 25
# ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000?
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

#Filtros
profesion = "Abogado"
salario = 10000000

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, profesion=profesion)
df_filtrado = df_filtrado[df_filtrado['salario'] > salario]

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con profesión 'Abogado' y salario > 10,000,000: {cantidad_registros}")