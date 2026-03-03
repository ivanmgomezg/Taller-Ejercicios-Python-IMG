# ==================================================================================
# Módulo de filtros y búsquedas sobre el DataFrame
# ==================================================================================
import pandas as pd

def contar_con_filtros(df, **filtros):
    """
    Cuenta registros que cumplen múltiples condiciones.

    Parámetros:
        df (DataFrame): El DataFrame a filtrar
        **filtros: Condiciones como pares columna=valor

    Ejemplo:
        contar_con_filtros(df, ciudad='cali', nombre_cifrado='carlos')

    Retorna:
        int: Número de registros que cumplen todas las condiciones
    """
    mask = pd.Series([True] * len(df), index=df.index)
    for columna, valor in filtros.items():
        mask &= df[columna] == valor
    return mask.sum()