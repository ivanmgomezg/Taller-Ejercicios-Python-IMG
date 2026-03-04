# ==================================================================================
# Módulo de filtros y búsquedas sobre el DataFrame
# ==================================================================================
import pandas as pd

def filtrar(df, **filtros):
    """
    Filtra el DataFrame según múltiples condiciones de igualdad.
    La comparación es insensible a mayúsculas y minúsculas.

    Parámetros:
        df (DataFrame): El DataFrame a filtrar
        **filtros: Condiciones como pares columna=valor

    Ejemplo:
        filtrar(df, ciudad='Cali', nombre_cifrado='Carlos')

    Retorna:
        DataFrame: El DataFrame filtrado
    """
    df = df.copy()
    for columna, valor in filtros.items():
        # Verificamos si la columna es de tipo texto (object o str)
        if pd.api.types.is_string_dtype(df[columna]):
            # Comparamos en minúsculas para ignorar mayúsculas
            df = df[df[columna].str.lower() == str(valor).lower()]
        else:
            # Para columnas numéricas o booleanas comparamos directamente
            df = df[df[columna] == valor]
    return df