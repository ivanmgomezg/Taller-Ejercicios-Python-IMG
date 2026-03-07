import os
import subprocess
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_ejercicio(nombre_archivo):
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_base, 'soluciones', nombre_archivo)
    if os.path.exists(ruta_completa):
        limpiar_pantalla()
        print(f"==================================================")
        print(f"🚀 EJECUTANDO: {nombre_archivo}")
        print(f"==================================================\n")
        subprocess.run([".venv/bin/python", ruta_completa])
        print(f"\n\n==================================================")
        input("Presiona ENTER para volver al menú...")
    else:
        print(f"\n❌ ERROR: No se encontró el archivo: {ruta_completa}")
        time.sleep(3)

def menu_principal():
    ejercicios = [
        "Filas con ID no numérico",
        "Frecuencia nombre 'Maria'",
        "Frecuencia nombre 'Juan'",
        "Nombre más frecuente",
        "Apellido más frecuente",
        "Registros en Bogota",
        "Registros en Medellin",
        "Ciudades únicas",
        "Profesión 'Ingeniero'",
        "Profesión 'Programador'",
        "Profesiones únicas",
        "Emails con espacios",
        "Salarios no numéricos",
        "Salario promedio",
        "Salario máximo",
        "Salario mínimo",
        "Activos (Verdadero)",
        "Activos (Falso)",
        "Formato fecha incorrecto",
        "Nacidos entre 1990-2000",
        "Nacidos antes de 1960",
        "Personas > 50 años",
        "'Carlos' en 'Cali'",
        "'Ana' como 'Medico'",
        "'Abogado' salario > 10M",
        "'Barranquilla' activos >1980",
        "Ciudad más Ingenieros",
        "Profesión mejor salario",
        "Emails 'gmail.com'",
        "Jose Garcia",
    ]

    mitad = len(ejercicios) // 2

    while True:
        limpiar_pantalla()
        print("=" * 70)
        print("              MENÚ DE EJERCICIOS DEL TALLER                ")
        print("=" * 70)

        for i in range(mitad):
            izq = f"{i+1:02d}. {ejercicios[i]}"
            der = f"{i+mitad+1:02d}. {ejercicios[i+mitad]}"
            print(f"  {izq:<30} │  {der:<30}")

        print("-" * 70)
        print("  0. Salir")
        print("=" * 70)

        opcion = input("👉 Seleccione el número del ejercicio: ").strip()

        if opcion == "0":
            print("\nSaliendo del sistema...")
            break

        if opcion.isdigit():
            nombre_script = f"{opcion.zfill(2)}.py"
            ejecutar_ejercicio(nombre_script)
        else:
            print("\n⚠️ Entrada no válida. Use números del 01 al 30.")
            time.sleep(1.5)

if __name__ == "__main__":
    menu_principal()