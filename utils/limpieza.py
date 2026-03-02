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


def detectar_anomalias_texto(df, columna):
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


    

def corregir_txt(df, columna, umbral=45):
    """
    Corrige texto mal escritas comparándolas contra la lista de texto válidas.
    Usa fuzzy matching para encontrar la ciudad más parecida.

    Parámetros:
        df (DataFrame): El DataFrame a corregir
        columna (str): Nombre de la columna
        umbral (int): Porcentaje mínimo de similitud para aceptar la corrección (0-100)

    Retorna:
        DataFrame: El DataFrame con las textos corregidas
    """
    # Tomamos las campos más frecuentes como referencia (las válidas)
    texto_valido = df[columna].value_counts().head(20).index.tolist()

    def corregir(texto):
        resultado = process.extractOne(texto, texto_valido)
        if resultado and resultado[1] >= umbral:
            return resultado[0]
        return texto

    df[columna] = df[columna].apply(corregir)
    return df


def detectar_anomalias_numericas(df, columna):
    """
    Detecta y cuenta valores anómalos en una columna numérica.
    - Valores nulos
    - Valores negativos
    - Caracteres no numéricos

    Parámetros:
        df (DataFrame): El DataFrame a analizar
        columna (str): Nombre de la columna a revisar
    """
    nulos = df[columna].isna().sum()
    negativos = (pd.to_numeric(df[columna], errors='coerce') < 0).sum()
    no_numericos = pd.to_numeric(df[columna], errors='coerce').isna().sum() - nulos

    print(f"Anomalías detectadas en '{columna}':")
    print(f"  Valores nulos         : {nulos}")
    print(f"  Valores negativos     : {negativos}")
    print(f"  Caracteres no numéricos: {no_numericos}")


def normalizar_numericos(df, columnas):
    """
    Limpia y normaliza columnas numéricas en un DataFrame.
    - Elimina caracteres no numéricos excepto el punto decimal
    - Convierte la columna a tipo numérico
    - Reemplaza valores negativos por nulo

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columnas (list): Lista de columnas a normalizar. Ejemplo: ['salario', 'edad']

    Retorna:
        DataFrame: El DataFrame con las columnas normalizadas
    """
    def limpiar(valor):
        if isinstance(valor, str):
            # Quitamos todo excepto números y punto decimal
            valor = re.sub(r'[^0-9.]', '', valor)
        return valor

    for columna in columnas:
        df[columna] = df[columna].apply(limpiar)
        # Convertimos a numérico, los que no se puedan convertir quedan como nulo
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        # Reemplazamos negativos por nulo
        df[columna] = df[columna].where(df[columna] >= 0, other=pd.NA)

    return df


def normalizar_fechas(df, columna):
    """
    Limpia y normaliza una columna de fechas en un DataFrame.
    - Reemplaza separadores alternativos (puntos, barras) por guiones
    - Elimina caracteres no numéricos excepto el guión
    - Convierte la columna a tipo fecha
    - Valores que no se puedan convertir quedan como nulo

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columna (str): Nombre de la columna de fechas

    Retorna:
        DataFrame: El DataFrame con la columna de fechas normalizada
    """
    def limpiar(valor):
        if isinstance(valor, str):
            # Reemplazamos separadores alternativos por guión
            valor = re.sub(r'[./\\]', '-', valor)
            # Quitamos todo excepto números y guión
            valor = re.sub(r'[^0-9-]', '', valor)
        return valor

    df[columna] = df[columna].apply(limpiar)
    df[columna] = pd.to_datetime(df[columna], errors='coerce')

    return df



def normalizar_email(df, columna):
    """
    Limpia y normaliza una columna de emails en un DataFrame.
    - Elimina espacios al inicio y al final
    - Elimina caracteres extraños alrededor del email (paréntesis, corchetes)
    - Convierte a minúsculas
    - Marca como nulo los emails con formato inválido

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columna (str): Nombre de la columna de emails

    Retorna:
        DataFrame: El DataFrame con la columna de emails normalizada
    """
    def limpiar(valor):
        if isinstance(valor, str):
            # Quitamos espacios y convertimos a minúsculas
            valor = valor.strip().lower()
            # Eliminamos caracteres extraños alrededor del email
            valor = re.sub(r'[^\w\.\@\-\+]', '', valor)
            # Si no tiene formato válido de email lo marcamos como nulo
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', valor):
                return pd.NA
        return valor

    df[columna] = df[columna].apply(limpiar)
    return df


def normalizar_booleanos(df, columna):
    """
    Limpia y normaliza una columna booleana en un DataFrame.
    - Elimina caracteres especiales y espacios
    - Convierte variantes de texto a True/False
    - Valores no reconocidos quedan como nulo

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columna (str): Nombre de la columna booleana

    Retorna:
        DataFrame: El DataFrame con la columna booleana normalizada
    """
    verdaderos = ['true', '1', 'si', 'yes', 's', 'y']
    falsos = ['false', '0', 'no', 'n']

    def limpiar(valor):
        if isinstance(valor, str):
            # Quitamos espacios y caracteres especiales
            valor = re.sub(r'[^a-zA-Z0-9]', '', valor)
            valor = valor.strip().lower()
            if valor in verdaderos:
                return True
            elif valor in falsos:
                return False
            return pd.NA
        return valor

    df[columna] = df[columna].apply(limpiar)
    return df