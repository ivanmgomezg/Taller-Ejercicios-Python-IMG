

================================================================================
# ARCHIVO: 01.py
================================================================================

# ==================================================================================
# Ejercicio 01
# Descripción: ¿Cuántas filas tienen el campo id con caracteres no numéricos?
# ==================================================================================

# manejo de rutas y configuración del entorno de ejecución
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión desde la carpeta utils para cargar los datos
import utils.conexion as conexion 

# -------------------------------------------------------

df = conexion.cargar_datos_csv("personas.csv") # Cargamos el CSV en un DataFrame para poder manipularlo

id_no_num = (~df["id"].str.isnumeric()).sum() #En esta variable almaceno la cantidad de id que no(~) son numericos

print(f"De las 300.000 filas hay {id_no_num} filas con id que contienen caracteres no numéricos, lo que equivale al {(83648/300000)*100:.2f}% de todos los datos")

================================================================================
# ARCHIVO: 02.py
================================================================================

# ==================================================================================
# Ejercicio 02
# Descripción: ¿Cuántas veces aparece el nombre "Maria" en el dataset?
# ==================================================================================

# manejo de rutas y configuración del entorno de ejecución
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.limpieza as limp

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------

#Decodificamos la columna "nombre_cifrado" usando ROT13 para obtener los nombres reales 
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: limp.rot13(x)) 

# Nombre que queremos buscar en el dataset
nom_buscar = "Maria" 

# Contamos cuantas veces aparece "Maria" en la columna "nombre_cifrado"
contar = (df["nombre_cifrado"]==nom_buscar).sum() 

print(f"El nombre '{nom_buscar}' aparece {contar} veces en el dataset")

================================================================================
# ARCHIVO: 03.py
================================================================================

# ==================================================================================
# Ejercicio 03
# Descripción: ¿Cuántas veces aparece el nombre "Juan" en el dataset?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.limpieza as limp

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------


# Decodificamos la columna "nombre_cifrado" usando ROT13 para obtener los nombres reales 
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: limp.rot13(x)) 

# Nombre que queremos buscar en el dataset
nom_buscar = "Juan" 

# Contamos cuantas veces aparece "Juan" en la columna "nombre_cifrado"
contar = (df["nombre_cifrado"]==nom_buscar).sum() 

print(f"El nombre '{nom_buscar}' aparece {contar} veces en el dataset")

================================================================================
# ARCHIVO: 04.py
================================================================================

# ==================================================================================
# Ejercicio 04
# Descripción: ¿Cuál es el nombre más frecuente y cuántas veces aparece?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.limpieza as limp

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------

# Decodificamos la columna "nombre_cifrado" usando ROT13 para obtener los nombres reales 
df["nombre_cifrado"] = df["nombre_cifrado"].apply(lambda x: limp.rot13(x)) 

# Contamos la frecuencia de cada nombre en la columna "nombre_cifrado"
conteo = df["nombre_cifrado"].value_counts() 

# Obtenemos el nombre más frecuente utilizando idxmax() que devuelve el índice del valor máximo en la serie de conteo
nombre_mas_frecuente = conteo.idxmax() 

# Obtenemos la frecuencia del nombre más frecuente utilizando max() que devuelve el valor máximo en la serie de conteo
frecuencia = conteo.max() 

print(f"El nombre más frecuente es '{nombre_mas_frecuente}' y aparece {frecuencia} veces en el dataset") 

================================================================================
# ARCHIVO: 05.py
================================================================================

# ==================================================================================
# Ejercicio 05
# Descripción: ¿Cuál es el apellido más frecuente y cuántas veces aparece?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos el módulo de conexión y otros desde la carpeta utils para cargar los datos
import utils.conexion as conexion
import utils.limpieza as limp

# Cargamos el CSV en un DataFrame para poder manipularlo
df = conexion.cargar_datos_csv("personas.csv") 

# -------------------------------------------------------

df["apellido_cifrado"] = df["apellido_cifrado"].apply(lambda x: limp.rot13(x)) #Decodificamos la columna "apellido_cifrado" usando ROT13 para obtener los nombres reales 


# Contamos la frecuencia de cada nombre en la columna "apellido_cifrado"
conteo = df["apellido_cifrado"].value_counts() 

# Obtenemos el nombre más frecuente utilizando idxmax() que devuelve el índice del valor máximo en la serie de conteo
nombre_mas_frecuente = conteo.idxmax() 

# Obtenemos la frecuencia del nombre más frecuente utilizando max() que devuelve el valor máximo en la serie de conteo
frecuencia = conteo.max() 

print(f"El apellido más frecuente es '{nombre_mas_frecuente}' y aparece {frecuencia} veces en el dataset") 

================================================================================
# ARCHIVO: 06.py
================================================================================

# ==================================================================================
# Ejercicio 06
# ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion   

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función limpiar_dataset del módulo de limpieza

# Contamos cuántos registros tienen la ciudad "Bogota" en la columna "ciudad"
ciudad = 'bogota'
conteo_ciudad = df_clean[df_clean["ciudad"] == ciudad.lower()].shape[0]

print(f"El número de registros con la ciudad '{ciudad.capitalize()}' es: {conteo_ciudad}")


================================================================================
# ARCHIVO: 07.py
================================================================================

# ==================================================================================
# Ejercicio 07
# ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion   

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función limpiar_dataset del módulo de limpieza

# Contamos cuántos registros tienen la ciudad "Medellin" en la columna "ciudad"
ciudad = 'medellin'
conteo_ciudad = df_clean[df_clean["ciudad"] == ciudad.lower()].shape[0]

print(f"El número de registros con la ciudad '{ciudad.capitalize()}' es: {conteo_ciudad}")


================================================================================
# ARCHIVO: 08.py
================================================================================

# ==================================================================================
# Ejercicio 08
# ¿Cuántas ciudades únicas existen después de normalizar? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántas ciudades únicas existen en la columna "ciudad" después de normalizar
ciudades_unicas = df_clean["ciudad"].nunique()  
print(f"El número de ciudades únicas después de normalizar es: {ciudades_unicas}")

================================================================================
# ARCHIVO: 09.py
================================================================================

# ==================================================================================
# Ejercicio 09
# ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántos registros tienen la profesión "Ingeniero" después de limpiar
profesion = 'Ingeniero'
conteo = df_clean[df_clean["profesion"] == profesion.lower()].shape[0]
print(f"El número de registros con la profesión '{profesion.capitalize()}' después de limpiar es: {conteo}")

================================================================================
# ARCHIVO: 10.py
================================================================================

# ==================================================================================
# Ejercicio 10
# ¿Cuántos registros tienen la profesión "Programador" después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántos registros tienen la profesión "Ingeniero" después de limpiar
profesion = 'Programador'
conteo = df_clean[df_clean["profesion"] == profesion.lower()].shape[0]
print(f"El número de registros con la profesión '{profesion.capitalize()}' después de limpiar es: {conteo}")

================================================================================
# ARCHIVO: 11.py
================================================================================

# ==================================================================================
# Ejercicio 11
# ¿Cuántas profesiones únicas existen después de normalizar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántas profesiones únicas existen en la columna "profesion" después de normalizar
profesiones_unicas = df_clean["profesion"].nunique()  
print(f"El número de profesiones únicas después de normalizar es: {profesiones_unicas}")

================================================================================
# ARCHIVO: 12.py
================================================================================

# ==================================================================================
# Ejercicio 12
# ¿Cuántos registros tienen el campo email con espacios adicionales?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
contar = df["email"].str.contains(" ").sum()
print("Número de registros con espacios adicionales en el campo email: ", contar)

================================================================================
# ARCHIVO: 13.py
================================================================================

# ==================================================================================
# Ejercicio 13
# ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
contar = df["salario"].str.contains("[^0-9]").sum()
print("Número de registros con caracteres no numéricos en el campo salario:", contar)



================================================================================
# ARCHIVO: 14.py
================================================================================

# ==================================================================================
# Ejercicio 14
# ¿Cuál es el salario promedio después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

promedio = df_clean["salario"].mean()
print(f"El salario promedio después de limpiar es: {promedio:,.2f}")

================================================================================
# ARCHIVO: 15.py
================================================================================

# ==================================================================================
# Ejercicio 15
# ¿Cuál es el salario máximo después de limpiar? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

maximo = df_clean["salario"].max()
print(f"El salario máximo después de limpiar es: {maximo:,.2f}")

================================================================================
# ARCHIVO: 16.py
================================================================================

# ==================================================================================
# Ejercicio 16
# ¿Cuál es el salario mínimo después de limpiar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

minimo = df_clean["salario"].min()
print(f"El salario mínimo después de limpiar es: {minimo:,.2f}")

================================================================================
# ARCHIVO: 17.py
================================================================================

# ==================================================================================
# Ejercicio 17
# ¿Cuántos registros tienen `activo` como verdadero después de normalizar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántos registros tienen 'activo' como verdadero
registros = df_clean[df_clean["activo"] == True].shape[0]
print(f"El número de registros con 'activo' como verdadero después de normalizar es: {registros}")

================================================================================
# ARCHIVO: 18.py
================================================================================

# ==================================================================================
# Ejercicio 18
# ¿Cuántos registros tienen `activo` como falso después de normalizar?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df) # Limpiamos los datos utilizando la función

# Contamos cuántos registros tienen 'activo' como falso
registros = df_clean[df_clean["activo"] == False].shape[0]
print(f"El número de registros con 'activo' como falso después de normalizar es: {registros}")

================================================================================
# ARCHIVO: 19.py
================================================================================

# ==================================================================================
# Ejercicio 19
# ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")

# Sin limpiar, contamos los que NO tienen formato YYYY-MM-DD
formato_valido = df['fecha_nacimiento'].str.match(r'^\d{4}-\d{2}-\d{2}$', na=False).sum()
formato_diferente = len(df) - formato_valido

print(f"Registros con formato diferente a YYYY-MM-DD: {formato_diferente}")

================================================================================
# ARCHIVO: 20.py
================================================================================

# ==================================================================================
# Ejercicio 20
# ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Dejo en fecha de nacimiento solo el año para facilitar la comparación
df_clean['anio_nacimiento'] = df_clean['fecha_nacimiento'].dt.year

lim_inf = 1990
lim_sup = 2000

conteo = df_clean['anio_nacimiento'].between(lim_inf, lim_sup).sum()

print(f"Personas nacidas entre {lim_inf} y {lim_sup}: {conteo}")



================================================================================
# ARCHIVO: 21.py
================================================================================

# ==================================================================================
# Ejercicio 21
# ¿Cuántas personas nacieron antes de 1960? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Dejo en fecha de nacimiento solo el año para facilitar la comparación
df_clean['anio_nacimiento'] = df_clean['fecha_nacimiento'].dt.year


lim = 1960

# Realizo el conteo de las personas que nacieron antes de 1960
conteo = (df_clean['anio_nacimiento'] < lim).sum()

print(f"Hay {conteo} personas que nacieron antes de 1960")   

================================================================================
# ARCHIVO: 22.py
================================================================================

# ==================================================================================
# Ejercicio 21
# ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
from datetime import datetime

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

# Calculamos la edad de cada persona
fecha_actual = datetime(2026, 2, 26)

#nueva columna edad con el calculo de la edad a partir de la fecha de nacimiento
df_clean['edad'] = (fecha_actual - df_clean['fecha_nacimiento']).dt.days // 365

# Contamos cuántas personas tienen más de 50 años
personas_mayores_50 = df_clean[df_clean['edad'] > 50].shape[0]
print(f"El número de personas con más de 50 años es: {personas_mayores_50}")    


================================================================================
# ARCHIVO: 23.py
================================================================================

# ==================================================================================
# Ejercicio 23
# ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
from datetime import datetime

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
nombre_cifrado = "Carlos"
ciudad = "Cali"

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, nombre_cifrado=nombre_cifrado, ciudad=ciudad)

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con nombre 'Carlos' y ciudad 'Cali': {cantidad_registros}")

================================================================================
# ARCHIVO: 24.py
================================================================================

# ==================================================================================
# Ejercicio 24
# ¿Cuántos registros tienen nombre "Ana" y son "Medico"?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os
from datetime import datetime

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
nombre_cifrado = "Ana"
profesion = "Medico"

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, nombre_cifrado=nombre_cifrado, profesion=profesion)

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con nombre 'Ana' y profesión 'Medico': {cantidad_registros}")

================================================================================
# ARCHIVO: 25.py
================================================================================

# ==================================================================================
# Ejercicio 25
# ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
profesion = "Abogado"
salario = 10000000

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, profesion=profesion)
df_filtrado = df_filtrado[df_filtrado['salario'] > salario]

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con profesión 'Abogado' y salario > 10,000,000: {cantidad_registros}")

================================================================================
# ARCHIVO: 26.py
================================================================================

# ==================================================================================
# Ejercicio 26
# ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
ciudad = "Barranquilla"
activo = True
anio = 1980

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, ciudad=ciudad, activo=activo)
df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year > anio]

# Contamos el número de registros que cumplen con las condiciones
cantidad_registros = len(df_filtrado)

print(f"Cantidad de registros con ciudad 'Barranquilla', activos y nacidos después de 1980: {cantidad_registros}")

================================================================================
# ARCHIVO: 27.py
================================================================================

# ==================================================================================
# Ejercicio 27
# ¿Cuál es la ciudad con más "Ingenieros"?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

#Filtros
profesion = "Ingeniero"

# Filtramos el DataFrame para obtener solo los registros que cumplen con las condiciones
df_filtrado = filt.filtrar(df_clean, profesion=profesion)

# Contamos el número de ingenieros por ciudad
conteo_ciudades = df_filtrado['ciudad'].value_counts()

# Encontramos la ciudad con más ingenieros
ciudad_max_ingenieros = conteo_ciudades.idxmax()
cantidad_ingenieros = conteo_ciudades.max()

print(f"La ciudad con más ingenieros es '{ciudad_max_ingenieros}' con {cantidad_ingenieros} ingenieros.")

================================================================================
# ARCHIVO: 28.py
================================================================================

# ==================================================================================
# Ejercicio 28
# ¿Cuál es la profesión con el salario promedio más alto? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

# Agrupamos por profesión y calculamos el salario promedio
salario_promedio = df_clean.groupby('profesion')['salario'].mean()

# Encontramos la profesión con el salario promedio más alto
profesion_mas_alta = salario_promedio.idxmax()
salario_mas_alto = salario_promedio.max()

print(f"La profesión con el salario promedio más alto es: {profesion_mas_alta} con un salario promedio de {salario_mas_alto:.2f}")


================================================================================
# ARCHIVO: 29.py
================================================================================

# ==================================================================================
# Ejercicio 29
# ¿Cuántos registros tienen email con dominio "gmail.com"?
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

# Filtramos los registros con email que termina en "gmail.com"
filtro_gmail = df_clean['email'].str.endswith('@gmail.com', na=False)
registros_gmail = df_clean[filtro_gmail]

# Contamos el número de registros con email de gmail
cantidad_gmail = len(registros_gmail)

print(f"El número de registros con email de gmail es: {cantidad_gmail}")

================================================================================
# ARCHIVO: 30.py
================================================================================

# ==================================================================================
# Ejercicio 30
# ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? 
# ==================================================================================

# Importamos las librerias necesarias
import sys
import os

# Le decimos a Python dónde está la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.limpieza as limp
import utils.conexion as conexion
import utils.filtros as filt

#Conexion y limpieza de datos
df = conexion.cargar_datos_csv("personas.csv")
df_clean = limp.limpiar_dataset(df)

nombre = "Jose"
apellido = "Garcia"

df_filtro = filt.filtrar(df_clean, nombre_cifrado=nombre, apellido_cifrado=apellido)
contar = len(df_filtro)

print(f"El número de registros con nombre {nombre} y apellido {apellido} es: {contar}")

