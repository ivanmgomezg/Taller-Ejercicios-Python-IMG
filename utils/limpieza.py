# ==================================================================================
# Módulo de limpieza y normalización de datos
# ==================================================================================

import pandas as pd
import unicodedata

def normalizar_texto(df, columnas):
    """
    Limpia y normaliza columnas de texto en un DataFrame.
    - Elimina espacios al inicio y al final
    - Convierte todo a minúsculas
    - Elimina tildes y caracteres especiales

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
