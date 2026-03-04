# ==================================================================================
# Ejercicio 28
# ¿Cuál es la profesión con el salario promedio más alto? 
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

# Agrupamos por profesión y calculamos el salario promedio
salario_promedio = df_clean.groupby('profesion')['salario'].mean()

# Encontramos la profesión con el salario promedio más alto
profesion_mas_alta = salario_promedio.idxmax()
salario_mas_alto = salario_promedio.max()

print(f"La profesión con el salario promedio más alto es: {profesion_mas_alta} con un salario promedio de {salario_mas_alto:.2f}")
