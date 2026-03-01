# sandbox.py - archivo de pruebas y experimentos, no forma parte de las soluciones

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import utils.conexion as conexion
import utils.limpieza as limp

df = conexion.cargar_datos_csv("personas.csv")

