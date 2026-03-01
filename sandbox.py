# sandbox.py - archivo de pruebas y experimentos, no forma parte de las soluciones

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import utils.conexion as conexion
import utils.limpieza as limp

df = conexion.cargar_datos_csv("personas.csv")

limp.detectar_anomalias(df, 'ciudad')
limp.normalizar_texto(df, ['ciudad'])
limp.detectar_anomalias(df, 'ciudad')


import re

def ver_caracteres_especiales(df, columna):
    """Muestra los valores únicos que aún contienen caracteres especiales"""
    mask = df[columna].str.contains(r'[^a-zA-Z\s]', regex=True, na=False)
    print(df[columna][mask].unique())

df = limp.corregir_ciudades(df, 'ciudad')
conteo_ciudades = df["ciudad"].value_counts().reset_index()
conteo_ciudades.columns = ["ciudad", "conteo"]
print(conteo_ciudades.to_string())


ver_caracteres_especiales(df, 'ciudad')


# Agrupamos las ciudades y contamos cuántas veces aparece cada una
conteo_ciudades = df["ciudad"].value_counts().reset_index()
conteo_ciudades.columns = ["ciudad", "conteo"]
print(conteo_ciudades.to_string())