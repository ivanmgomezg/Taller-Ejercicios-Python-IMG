# ==================================================================================
# Módulo de conexión y carga de datos
# ==================================================================================

#Importamos las librerias necesarias para el trabajo con datos
import pandas as pd 
import numpy as np

#Nombre del archivo con los datos
ruta = "./data/" 

def cargar_datos_csv(archivo):
    """
    Carga un archivo csv desde la carpeta data y lo retorna como un DataFrame de pandas.
    El archivo debe estar ubicado en la carpeta data y debe ser un archivo CSV.
    
    Parámetros:
        archivo (str): Nombre del archivo CSV. Ejemplo: 'personas.csv'
    
    Retorna:
        DataFrame: Contenido del archivo listo para manipular.
    """

    df = pd.read_csv(ruta+archivo) # Cargamos el CSV en un DataFrame para poder manipularlo
    return df