# ==================================================================================
# Módulo de limpieza y normalización de datos
# ==================================================================================

import pandas as pd
from thefuzz import process
import unicodedata
import re

def normalizar_texto(df, columnas):
    """
    Limpia y normaliza columnas de texto en un DataFrame.
    - Elimina espacios al inicio y al final
    - Convierte a minúsculas
    - Elimina tildes y caracteres especiales
    - Elimina números
    - Elimina cualquier caracter que no sea letra o espacio

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columnas (list): Lista de columnas a normalizar. Ejemplo: ['ciudad', 'profesion']

    Retorna:
        DataFrame: El DataFrame con las columnas normalizadas
    """
    def limpiar(texto):
        if isinstance(texto, str):
            # Quitamos espacios al inicio y al final
            texto = texto.strip()
            # Convertimos a minúsculas
            texto = texto.lower()
            # Quitamos tildes y caracteres especiales
            texto = unicodedata.normalize('NFD', texto)
            texto = texto.encode('ascii', 'ignore').decode('utf-8')
            # Quitamos números
            texto = ''.join([c for c in texto if not c.isdigit()])
            # Quitamos cualquier caracter que no sea letra o espacio
            texto = re.sub(r'[^a-zA-Z\s]', '', texto)
        return texto

    for columna in columnas:
        df[columna] = df[columna].apply(limpiar)

    return df


def detectar_anomalias(df, columna):
    """
    Detecta y cuenta valores con caracteres anómalos en una columna.
    - Espacios al inicio o al final
    - Tildes o caracteres especiales
    - Números dentro del texto

    Parámetros:
        df (DataFrame): El DataFrame a analizar
        columna (str): Nombre de la columna a revisar

    Retorna:
        dict: Resumen con conteos de cada tipo de anomalía
    """
    espacios = df[columna].str.match(r'^\s|\s$').sum()
    tildes = df[columna].str.contains(r'[áéíóúÁÉÍÓÚüÜñÑ]', regex=True).sum()
    numeros = df[columna].str.contains(r'\d', regex=True).sum()
    especiales = df[columna].str.contains(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]', regex=True).sum()

    print(f"Anomalías detectadas en '{columna}':")
    print(f"  Espacios al inicio o final : {espacios}")
    print(f"  Tildes                     : {tildes}")
    print(f"  Números                    : {numeros}")
    print(f"  Caracteres especiales      : {especiales}")


    

def corregir_ciudades(df, columna, umbral=60):
    """
    Corrige ciudades mal escritas comparándolas contra la lista de ciudades válidas.
    Usa fuzzy matching para encontrar la ciudad más parecida.

    Parámetros:
        df (DataFrame): El DataFrame a corregir
        columna (str): Nombre de la columna de ciudades
        umbral (int): Porcentaje mínimo de similitud para aceptar la corrección (0-100)

    Retorna:
        DataFrame: El DataFrame con las ciudades corregidas
    """
    # Tomamos las ciudades más frecuentes como referencia (las válidas)
    ciudades_validas = df[columna].value_counts().head(20).index.tolist()

    def corregir(ciudad):
        resultado = process.extractOne(ciudad, ciudades_validas)
        if resultado and resultado[1] >= umbral:
            return resultado[0]
        return ciudad

    df[columna] = df[columna].apply(corregir)
    return df