import os

ruta_soluciones = os.path.join(os.path.dirname(__file__), 'soluciones')
archivos = sorted([f for f in os.listdir(ruta_soluciones) if f.endswith('.py')])

with open('todos_ejercicios.py', 'w') as salida:
    for archivo in archivos:
        ruta = os.path.join(ruta_soluciones, archivo)
        with open(ruta, 'r') as f:
            contenido = f.read()
        salida.write(f"\n\n{'='*80}\n")
        salida.write(f"# ARCHIVO: {archivo}\n")
        salida.write(f"{'='*80}\n\n")
        salida.write(contenido)

print("Archivo generado: todos_ejercicios.py")