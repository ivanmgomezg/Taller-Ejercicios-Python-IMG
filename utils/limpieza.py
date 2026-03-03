# ==================================================================================
# Módulo de limpieza, normalización y transformación de datos
# ==================================================================================

import codecs
import pandas as pd
import numpy as np
import re
import unicodedata
import codecs #Para la decodificación ROT13
from thefuzz import process, fuzz

# Configuración de visualización de números
pd.set_option('display.float_format', lambda x: f'{x:.0f}')


#Defino una función para decodificar el texto usando ROT13
def rot13(texto): 
    return codecs.decode(texto, "rot13")


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
    Detecta y cuenta valores con caracteres anómalos en una columna de texto.
    - Espacios al inicio o al final
    - Tildes o caracteres especiales
    - Números dentro del texto

    Parámetros:
        df (DataFrame): El DataFrame a analizar
        columna (str): Nombre de la columna a revisar
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


def corregir_fuzzy(df, columna, umbral=80, min_frecuencia=1000):
    """
    Corrige valores mal escritos comparándolos contra los más frecuentes.
    Usa fuzzy matching con token_set_ratio para mejor detección de palabras
    con letras faltantes o transpuestas.

    Parámetros:
        df (DataFrame): El DataFrame a corregir
        columna (str): Nombre de la columna
        umbral (int): Porcentaje mínimo de similitud para aceptar la corrección (0-100)
        min_frecuencia (int): Frecuencia mínima para considerar un valor como válido

    Retorna:
        DataFrame: El DataFrame con los valores corregidos
    """
    
    conteo = df[columna].value_counts()
    texto_valido = conteo[conteo > min_frecuencia].index.tolist()

    def corregir(texto):
        texto = str(texto).strip().lower()

        if texto in texto_valido:
            return texto

        resultado = process.extractOne(texto, texto_valido, scorer=fuzz.token_set_ratio)

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
    print(f"  Valores nulos          : {nulos}")
    print(f"  Valores negativos      : {negativos}")
    print(f"  Caracteres no numéricos: {no_numericos}")


def normalizar_moneda(df, columnas):
    """
    ...
    - Detecta y extrae números después de prefijos de texto. Ejemplo: aprox.10001178 -> 10001178
    - Remplaza letras similares a números (l->1, o->0)
    - Elimina símbolos de moneda y caracteres especiales. Ejemplo: $, @, [, ]
    - Maneja formatos con puntos de miles y comas decimales. Ejemplo: 1.250,50
    - Maneja múltiples puntos decimales por error. Ejemplo: 1.250.500
    - Convierte la columna a tipo numérico
    - Reemplaza valores negativos por nulo
    ...

    Parámetros:
        df (DataFrame): El DataFrame a limpiar
        columnas (list): Lista de columnas a normalizar. Ejemplo: ['salario', 'precio']

    Retorna:
        DataFrame: El DataFrame con las columnas normalizadas
    """
    def limpiar_valor(valor):
        if pd.isna(valor):
            return np.nan

        # Convertimos a string y limpiamos espacios
        valor_str = str(valor).strip().lower()

        # Caso especial: texto seguido de punto y número. Ejemplo: aprox.10001178
        # Tomamos directamente lo que está después del punto
        match = re.search(r'[a-z]+\.(\d+)', valor_str)
        if match:
            return match.group(1)

        # Reemplazamos letras similares a números
        valor_str = valor_str.replace('l', '1').replace('o', '0')

        # Eliminamos símbolos al inicio y al final
        valor_str = re.sub(r'^[^0-9]+|[^0-9]+$', '', valor_str)

        if not valor_str:
            return np.nan

        # Caso 1: puntos de miles y coma decimal. Ejemplo: 1.250,50
        if '.' in valor_str and ',' in valor_str:
            valor_str = valor_str.replace('.', '')
            valor_str = valor_str.replace(',', '.')

        # Caso 2: solo coma decimal. Ejemplo: 1250,50
        elif ',' in valor_str:
            valor_str = valor_str.replace(',', '.')

        # Quitamos todo excepto números y punto decimal
        valor_limpio = re.sub(r'[^0-9.]', '', valor_str)

        # Si quedaron múltiples puntos dejamos solo el último
        if valor_limpio.count('.') > 1:
            partes = valor_limpio.split('.')
            valor_limpio = "".join(partes[:-1]) + "." + partes[-1]

        if not valor_limpio or valor_limpio == '.':
            return np.nan

        return valor_limpio

    df_resultado = df.copy()

    for columna in columnas:
        if columna in df_resultado.columns:
            df_resultado[columna] = df_resultado[columna].apply(limpiar_valor)
            # Convertimos a numérico, los que no se puedan convertir quedan como nulo
            df_resultado[columna] = pd.to_numeric(df_resultado[columna], errors='coerce')
            # Los salarios negativos no son válidos
            df_resultado.loc[df_resultado[columna] < 0, columna] = np.nan

    return df_resultado


def normalizar_identificadores(df, columnas):
    """
    Limpia y normaliza columnas de identidad (IDs) en un DataFrame.
    - Maneja casos como '145,00' convirtiéndolos en '145'.
    - Elimina texto como 'aprox.' o símbolos como '@', '#', '[]'.
    - Convierte a tipo 'Int64' (Entero con soporte para nulos).
    """
    
    if isinstance(columnas, str):
        columnas = [columnas]

    def limpiar_valor_individual(valor):
        if pd.isna(valor):
            return None
        
        # 1. Convertimos a string y limpiamos espacios
        texto = str(valor).strip().lower()
        
        # 2. Manejo de decimales accidentales:
        # Si tiene una coma (como 145,00), nos quedamos solo con lo de la izquierda
        texto = texto.split(',')[0]
        
        # 3. REGEX: Borramos todo lo que NO sea un número
        # Esto quita el punto de 'aprox.', los corchetes, etc.
        texto_limpio = re.sub(r'[^0-9]', '', texto)
        
        return texto_limpio if texto_limpio != '' else None

    for col in columnas:
        if col in df.columns:
            # Aplicamos la limpieza fila por fila
            df[col] = df[col].apply(limpiar_valor_individual)
            
            # Convertimos a numérico y luego a Int64
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
    
    return df


def normalizar_fechas(df, columna):
    """
    Limpia y normaliza una columna de fechas con formatos ruidosos.
    - Elimina espacios accidentales (ej: '19 92' -> '1992').
    - Estandariza separadores no convencionales.
    - Remueve símbolos de ruido como '??', '~', '@', '%'.
    - Convierte el resultado al tipo de dato datetime de Pandas.

    Parámetros:
        df (DataFrame): El DataFrame a procesar.
        columna (str): El nombre de la columna de fechas (ej: 'fecha_nacimiento').

    Retorna:
        DataFrame: El DataFrame con la columna convertida a objetos datetime.
    """
    
    def limpiar_fecha_string(valor):
        """
        Función interna para sanear strings individuales antes de la conversión.
        """
        # Si el valor ya es nulo (NaN/None), no intentamos procesarlo
        if pd.isna(valor): 
            return None
        
        # Convertimos a string y eliminamos espacios exteriores
        texto = str(valor).strip()
        
        # 1. Corrección de espacios internos:
        # Algunos registros vienen como '20 01-10-19'. Al quitar el espacio,
        # recuperamos el año correcto '2001-10-19'.
        texto = texto.replace(" ", "")
        
        # 2. Homogeneización de separadores:
        # Usamos regex para cambiar cualquier punto (.), barra (/) o diagonal inversa (\)
        # por un guion (-), unificando el formato a 'YYYY-MM-DD'.
        texto = re.sub(r'[./\\]', '-', texto)
        
        # 3. Limpieza de caracteres residuales (Regex):
        # El patrón [^0-9-] busca cualquier cosa que NO sea un número del 0-9 o un guion.
        # Esto elimina de forma masiva los '??', '~', '@', '%', etc.
        texto = re.sub(r'[^0-9-]', '', texto)
        
        return texto

    # Verificamos la existencia de la columna para evitar errores de ejecución
    if columna in df.columns:
        # Fase 1: Aplicamos la limpieza de texto celda por celda
        df[columna] = df[columna].apply(limpiar_fecha_string)
        
        # Fase 2: Conversión a tipo Datetime nativo de Pandas
        # - dayfirst=False: Prioriza el formato ISO (Año primero), típico de este dataset.
        # - errors='coerce': Si una fecha es lógica pero imposible (ej: 2023-02-30),
        #   la convierte en NaT (Not a Time) en lugar de detener el script con un error.
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
            valor = valor.strip().lower()
            # Eliminamos prefijo mailto: si existe
            valor = re.sub(r'^mailto:', '', valor)
            valor = re.sub(r'[^\w\.\@\-\+]', '', valor)
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


def limpiar_dataset(df):
    """
    Aplica toda la limpieza y normalización al dataset completo.

    Parámetros:
        df (DataFrame): El DataFrame a limpiar

    Retorna:
        DataFrame: El DataFrame completamente limpio

    Notas:
        - ciudad: umbral 60, nombres largos y reconocibles
        - profesion: umbral 45, palabras más cortas requieren menor umbral
    """    
    df = normalizar_identificadores(df, 'id')

    df['nombre_cifrado'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(x, 'rot13'))
    df['apellido_cifrado'] = df['apellido_cifrado'].apply(lambda x: codecs.decode(x, 'rot13'))

    df = normalizar_texto(df, ['ciudad', 'profesion'])
    df = corregir_fuzzy(df, 'ciudad', umbral=70)
    df = corregir_fuzzy(df, 'profesion', umbral=80)
    df = normalizar_email(df, 'email')
    df = normalizar_fechas(df, 'fecha_nacimiento')
    df = normalizar_moneda(df, ['salario'])
    df = normalizar_booleanos(df, 'activo')    
    return df