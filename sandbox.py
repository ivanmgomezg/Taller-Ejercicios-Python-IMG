# sandbox.py - archivo de pruebas y experimentos, no forma parte de las soluciones

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import utils.conexion as conexion
import utils.limpieza as limp
import pandas as pd

df = conexion.cargar_datos_csv("personas.csv")

print(df.head(20))

# ------------------------------------------------------------------------------
# Validar normalizacion columas texto

#Detectamos anomalías antes de la limpieza
limp.detectar_anomalias_texto(df, col_analizar)

# Normalizamos la columna 
limp.normalizar_texto(df, [col_analizar])

#Detectamos anomalías depues de la limpieza
limp.detectar_anomalias_texto(df, col_analizar)


import re

def ver_caracteres_especiales(df, columna):
    """Muestra los valores únicos que aún contienen caracteres especiales"""
    mask = df[columna].str.contains(r'[^a-zA-Z\s]', regex=True, na=False)
    print(df[columna][mask].unique())

# Corregimos las ciudades con tildes o caracteres especiales umbral 60% de similitud
df = limp.corregir_txt(df, col_analizar)

print("cuenta caracteres especiales:")
print(ver_caracteres_especiales(df, col_analizar))

# Agrupamos las ciudades y contamos cuántas veces aparece cada una
conteo = df[col_analizar].value_counts().reset_index()
conteo.columns = [col_analizar, "conteo"]

print("Suma total de registros:", conteo["conteo"].sum())

print(conteo.to_string())


# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# Validar normalizacion columas numericas

limp.detectar_anomalias_numericas(df, col_analizar)
df = limp.normalizar_numericos(df, [col_analizar])
limp.detectar_anomalias_numericas(df, col_analizar)

def contar_no_numericos(df, columna):
    """
    Cuenta y muestra los valores que contienen caracteres no numéricos en una columna.

    Parámetros:
        df (DataFrame): El DataFrame a analizar
        columna (str): Nombre de la columna a revisar
    """
    mask = pd.to_numeric(df[columna], errors='coerce').isna() & df[columna].notna()
    total = mask.sum()
    print(f"Valores no numéricos en '{columna}': {total}")
    if total > 0:
        print(df[columna][mask].unique())


contar_no_numericos(df, col_analizar)
df = limp.normalizar_numericos(df, [col_analizar])
contar_no_numericos(df, col_analizar)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Validar normalizacion columas fechas

limp.detectar_anomalias_numericas(df, 'fecha_nacimiento')
df = limp.normalizar_fechas(df, 'fecha_nacimiento')
print(df['fecha_nacimiento'].head())


def distribucion_edad_por_fecha(df, columna_fecha):
    """
    Calcula la edad a partir de la fecha de nacimiento,
    agrupa por rangos de 10 años y muestra la distribución.

    Parámetros:
        df (DataFrame): El DataFrame a analizar
        columna_fecha (str): Nombre de la columna de fecha de nacimiento
    """
    hoy = pd.Timestamp.today()
    edad = (hoy - df[columna_fecha]).dt.days // 365

    bins = list(range(0, 121, 10))
    labels = [f"{i}-{i+9}" for i in range(0, 120, 10)]

    rangos = pd.cut(edad, bins=bins, labels=labels, right=False)
    conteo = rangos.value_counts().sort_index()

    print(f"Distribución de edades calculadas desde '{columna_fecha}':")
    for rango, cantidad in conteo.items():
        print(f"  {rango} años : {cantidad}")
    print(f"  {'─'*30}")
    print(f"  Total con fecha válida : {conteo.sum()}")
    print(f"  Fechas nulas           : {df[columna_fecha].isna().sum()}")
    print(f"  Total registros        : {len(df)}")


distribucion_edad_por_fecha(df, 'fecha_nacimiento')

# Mostramos los valores originales que no se pudieron convertir a fecha
nulos_fecha = df[df['fecha_nacimiento'].isna()]
print(f"Valores con fecha nula:")
print(nulos_fecha['fecha_nacimiento'].head(20))

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Validar normalizacion email

df = limp.normalizar_email(df, 'email')
print(df[['email']].head(50))

# Validación de emails
print("=" * 50)
print("EMAIL - Validación")
print("=" * 50)

# Conteo general
total = len(df)
validos = df['email'].notna().sum()
nulos = df['email'].isna().sum()

print(f"  Emails válidos  : {validos}")
print(f"  Emails inválidos: {nulos}")
print(f"  Total registros : {total}")

# Mostramos ejemplos de emails inválidos antes de limpiar
print("\nEjemplos de emails inválidos:")
print(df[df['email'].isna()]['email'].head(10))

# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Validar normalizacion fecha

# Mostramos ejemplos de registros con activo nulo
print("\nEjemplos de registros con activo nulo:")


# Validación activo - Antes
print("=" * 50)
print("ACTIVO - Antes de limpiar")
print("=" * 50)
print(df['activo'].value_counts(dropna=False))

df = limp.normalizar_booleanos(df, 'activo')

# Validación activo - Después
print("\nACTIVO - Después de limpiar")
print("=" * 50)
print(df['activo'].value_counts(dropna=False))
print(f"\n  True            : {df['activo'].sum()}")
print(f"  False           : {(df['activo'] == False).sum()}")
print(f"  Nulos           : {df['activo'].isna().sum()}")
print(f"  Total registros : {len(df)}")

# ------------------------------------------------------------------------------
