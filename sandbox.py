# sandbox.py - archivo de pruebas y experimentos, no forma parte de las soluciones

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import utils.conexion as conexion
import utils.limpieza as limp
import pandas as pd
from thefuzz import process, fuzz

# ------------------------------------------------------------------------------
# Pruebas validar normalizacion columas texto
# ------------------------------------------------------------------------------

def pruebas_col_texto(df, col_analizar, umbral=70):

    print("--- Lista de nombres únicos ---")
    print(df[col_analizar].unique())

    print("\n--- ¿Cuántas variantes hay? ---")
    print(df[col_analizar].nunique())

    print("\n--- Frecuencia de cada nombre ---")
    print(df[col_analizar].value_counts())


    #Detectamos anomalías antes de la limpieza
    limp.detectar_anomalias_texto(df, col_analizar)

    
    import re

    def ver_caracteres_especiales(df, columna):
        """Muestra los valores únicos que aún contienen caracteres especiales"""
        mask = df[columna].str.contains(r'[^a-zA-Z\s]', regex=True, na=False)
        print(df[columna][mask].unique())

    print("cuenta caracteres especiales:")
    print(ver_caracteres_especiales(df, col_analizar))

    #####
    # Normalizamos la columna     
    df = limp.normalizar_texto(df, [col_analizar])

    # Corregimos las textos con tildes o caracteres especiales umbral 60% de similitud
    df = limp.corregir_fuzzy(df, col_analizar, umbral=umbral)
    # Umbral ciudad=70 | # profesion =80
    ####

    #Detectamos anomalías depues de la limpieza
    limp.detectar_anomalias_texto(df, col_analizar)
  
    # Agrupamos las campos y contamos cuántas veces aparece cada una
    conteo = df[col_analizar].value_counts().reset_index()
    conteo.columns = [col_analizar, "conteo"]

    print("Suma total de registros:", conteo["conteo"].sum())

    print(conteo.to_string())

# ------------------------------------------------------------------------------
# verificar_umbral() muestra el porcentaje de similitud entre cada variante incorrecta y su corrección
# sugerida por fuzzy matching. Útil para determinar el umbral adecuado antes de aplicar corregir_fuzzy().
# El porcentaje más bajo del output indica el umbral mínimo que debes usar en corregir_fuzzy() 
# para que todas las variantes sean corregidas correctamente.
# Ejemplo: si el mínimo es 71%, usa umbral=70 en corregir_fuzzy().
# ------------------------------------------------------------------------------

def verificar_umbral(df_temp, col_analizar):
    """
    Muestra el porcentaje de similitud entre cada variante incorrecta y su corrección
    sugerida por fuzzy matching. Útil para determinar el umbral adecuado antes de
    aplicar corregir_fuzzy().

    El porcentaje más bajo del output indica el umbral mínimo que debes usar en
    corregir_fuzzy() para que todas las variantes sean corregidas correctamente.

    Ejemplo: si el mínimo es 71%, usa umbral=70 en corregir_fuzzy().

    Parámetros:
        df_temp (DataFrame): El DataFrame a analizar, debe estar normalizado previamente
        col_analizar (str): Nombre de la columna a verificar
    """
    conteo = df_temp[col_analizar].value_counts()

    # Valores con más de 1000 registros se consideran válidos
    campos_validas = conteo[conteo > 1000].index.tolist()
    # Valores con menos de 1000 registros se consideran variantes a corregir
    variantes = conteo[conteo <= 1000].index.tolist()

    print("Verificando correcciones:")
    for v in variantes:
        # token_set_ratio compara ignorando el orden y longitud de las palabras
        resultado = process.extractOne(v, campos_validas, scorer=fuzz.token_set_ratio)
        print(f"  {v:20} → {resultado[0]:20} ({resultado[1]}%)")

# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# Pruebas validar normalizacion columas numericas
# ------------------------------------------------------------------------------

def pruebas_col_numero(df, col_analizar):

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
# Pruebas validar normalizacion columas fechas
# ------------------------------------------------------------------------------

def pruebas_col_fecha(df, col_analizar):
    print("=" * 50)
    print(f"ANTES de limpiar '{col_analizar}'")
    print("=" * 50)
    print(f"  Nulos   : {df[col_analizar].isna().sum()}")
    print(f"  Muestra :\n{df[col_analizar].head()}")

    df = limp.normalizar_fechas(df, col_analizar)

    print(f"\nDESPUÉS de limpiar '{col_analizar}'")
    print("=" * 50)
    print(f"  Nulos   : {df[col_analizar].isna().sum()}")
    print(f"  Muestra :\n{df[col_analizar].head()}")

    # Agrupamos por rangos de décadas
    df['decada'] = (df[col_analizar].dt.year // 10 * 10).astype('Int64')
    conteo_decadas = df['decada'].value_counts().sort_index().reset_index()
    conteo_decadas.columns = ['decada', 'conteo']

    print(f"\nDistribución por década de nacimiento:")
    for _, row in conteo_decadas.iterrows():
        print(f"  {int(row['decada'])}s : {row['conteo']}")
    print(f"  {'─'*30}")
    print(f"  Total con fecha válida : {conteo_decadas['conteo'].sum()}")
    print(f"  Fechas nulas           : {df[col_analizar].isna().sum()}")
    print(f"  Total registros        : {len(df)}")

    # Eliminamos la columna temporal
    df.drop(columns=['decada'], inplace=True)

# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# Pruebas validar normalizacion email
# ------------------------------------------------------------------------------

def pruebas_col_email(df, col_analizar):

    df = limp.normalizar_email(df, col_analizar)
    print(df[[col_analizar]].head(50))

    # Validación de emails
    print("=" * 50)
    print("EMAIL - Validación")
    print("=" * 50)

    # Conteo general
    total = len(df)
    validos = df[col_analizar].notna().sum()
    nulos = df[col_analizar].isna().sum()

    print(f"  Emails válidos  : {validos}")
    print(f"  Emails inválidos: {nulos}")
    print(f"  Total registros : {total}")

    # Mostramos ejemplos de emails inválidos antes de limpiar
    print("\nEjemplos de emails inválidos:")
    print(df[df[col_analizar].isna()][col_analizar].head(10))
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pruebas validar booelanos activo
# ------------------------------------------------------------------------------

def pruebas_col_booleana(df, col_analizar):
    
    df = limp.normalizar_booleanos(df, 'activo')

    """
    Valida si una columna es booleana, cuenta valores y detecta 'basura'.
    """
    print(f"\n--- Analizando columna booleana: '{col_analizar}' ---")

    # 1. ¿Cómo contar True y False? 
    # Al sumar, contamos los True automáticamente porque valen 1
    total_true = df[col_analizar].sum()
    total_rows = len(df[col_analizar])
    total_false = total_rows - total_true - df[col_analizar].isna().sum()

    print(f"Total True (1): {total_true}")
    print(f"Total False (0): {total_false}")
    print(f"Valores Nulos (NaN): {df[col_analizar].isna().sum()}")

    # 2. Validar si hay valores que NO son booleanos
    # Verificamos si los valores únicos son diferentes de True, False o NaN
    valores_unicos = df[col_analizar].unique()
    print(f"Valores únicos encontrados: {valores_unicos}")

    # 3. Detectar "Anomalías" (cosas que no son True/False)
    mask_no_bool = ~df[col_analizar].isin([True, False, 1, 0, None])
    anomalias = df[col_analizar][mask_no_bool]
    
    if not anomalias.empty:
        print(f"⚠️ ¡Cuidado! Valores no booleanos detectados: {anomalias.unique()}")
    else:
        print("✅ La columna tiene un formato booleano correcto.")



df = conexion.cargar_datos_csv("personas.csv")
pruebas_col_booleana(df,"activo")   