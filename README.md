## Requisitos

Este proyecto usa un entorno virtual de Python. Para configurarlo:

### 1. Crear el entorno virtual
```bash
python -m venv .venv
```

### 2. Activar el entorno virtual
```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar un ejercicio
```bash
python soluciones/01.py
```

> ⚠️ **Importante:** Asegúrate de que el entorno virtual esté activado antes de ejecutar cualquier script. Si ves un error de `KeyboardInterrupt` al importar pandas, activa el entorno con `source .venv/bin/activate` y vuelve a ejecutar.

> Asegúrate de ejecutar los scripts siempre desde la raíz del proyecto y con el entorno virtual activado.


# Taller de Python - Manejo y Limpieza de Datos

## Infraestructura para Grandes Volúmenes de Datos

---

## Instrucciones de Entrega

**Fecha límite:** Jueves 5 de marzo, 11:59 PM

### Paso 1: Fork del Repositorio

Debe hacer un **fork** de este repositorio a su cuenta de GitHub.

¿No sabes cómo hacer un fork? Mira este video tutorial: [Cómo hacer un Fork en GitHub](https://www.youtube.com/watch?v=3m7Z3g_U-Cs)

### Paso 2: Completar las Soluciones

Clone su fork y complete los 30 ejercicios en la carpeta `soluciones/`. Actualice el README con las respuestas correctas.

### Paso 3: Pull Request

Una vez completado, cree un **Pull Request (PR)** hacia el repositorio principal. 

**Recursos útiles:**
- [Guía de Pull Requests en GitHub](https://www.youtube.com/watch?v=Zqft6yNRuNs)

**El PR debe incluir:**
- Código de las 30 soluciones en `soluciones/`
- README actualizado con todas las respuestas
- Descripción clara de su trabajo
- Cualquier mejora o documentación adicional que considere relevante

### Importante

⚠️ **Puede modificar cualquier archivo del repositorio EXCEPTO el archivo `data/personas.csv`**

Siéntase libre de mejorar:
- Documentación adicional
- Scripts de verificación
- Visualizaciones
- Organización del código
- Cualquier otra mejora que considere valiosa

---

## Rúbrica de Calificación

### Requisitos Mínimos (Aprobado)
- ✅ Las 30 soluciones implementadas en `soluciones/`
- ✅ Todas las respuestas verificadas y correctas
- ✅ README actualizado con las respuestas
- ✅ Código limpio y funcional

### Puntaje Extra (Ganador del PR)

**🏆 El Pull Request mejor presentado será aceptado y se convertirá en la versión oficial del taller.**

**Beneficios del ganador:**
- Su PR será merged al repositorio principal
- Su trabajo se convertirá en la referencia oficial del taller
- **+1.0 punto adicional en la calificación final**

**Criterios de evaluación para el mejor PR:**
- 📊 Calidad del código y organización
- 📝 Claridad de la documentación
- 🎨 Presentación profesional del repositorio
- 💡 Mejoras o aportes adicionales al proyecto
- ✨ Creatividad en la presentación de resultados

**Nota:** Todas las soluciones serán verificadas automáticamente. Resultados incorrectos descalificarán automáticamente al participante.

---

## Estructura del Repositorio

El repositorio debe contener:

```
├── soluciones/
│   ├── 01.py
│   ├── 02.py
│   ├── 03.py
│   ├── ...
│   └── 30.py
├── data/
│   └── personas.csv
└── README.md  (con las soluciones)
```

Cada archivo `.py` dentro de la carpeta `soluciones/` debe contener el código que resuelve el ejercicio correspondiente.

---

## Sobre el Dataset

- **Archivo:** `data/personas.csv`
- **Registros:** 300,000 filas
- **Columnas:** `id`, `nombre_cifrado`, `apellido_cifrado`, `ciudad`, `profesion`, `email`, `fecha_nacimiento`, `salario`, `activo`

### Datos sucios

El dataset tiene intencionalmente datos sucios en el 30% de cada columna:
- Espacios adicionales
- Caracteres especiales (@, %, #)
- Mayúsculas inconsistentes
- Formatos variados

### Descifrar nombres y apellidos

Los campos `nombre_cifrado` y `apellido_cifrado` usan cifrado ROT13:

```python
import codecs
nombre = codecs.decode(texto, 'rot_13')
```

---

## Ejercicios y Soluciones

A continuación se listan los 30 ejercicios. **Debe escribir el valor exacto de la respuesta** en la columna "Solución".

| # | Ejercicio | Solución |
|---|-----------|----------|
| 01 | ¿Cuántas filas tienen el campo `id` con caracteres no numéricos? | `83.648` |
| 02 | ¿Cuántas veces aparece el nombre "Maria" en el dataset? | `4.160` |
| 03 | ¿Cuántas veces aparece el nombre "Juan" en el dataset? | `3.986` |
| 04 | ¿Cuál es el nombre más frecuente y cuántas veces aparece? | `Gonzalo - 4.221` |
| 05 | ¿Cuál es el apellido más frecuente y cuántas veces aparece? | `Reyes - 7.490` |
| 06 | ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar? | `14.969` |
| 07 | ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar? | `15.193` |
| 08 | ¿Cuántas ciudades únicas existen después de normalizar? | `20` |
| 09 | ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar? | `12.083` |
| 10 | ¿Cuántos registros tienen la profesión "Programador" después de limpiar? | `12.062` |
| 11 | ¿Cuántas profesiones únicas existen después de normalizar? | `25` |
| 12 | ¿Cuántos registros tienen el campo `email` con espacios adicionales? | `45.447` |
| 13 | ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos? | `85.266` |
| 14 | ¿Cuál es el salario promedio después de limpiar? | `$ 8,005,689,17` |
| 15 | ¿Cuál es el salario máximo después de limpiar? | `14.999.952` |
| 16 | ¿Cuál es el salario mínimo después de limpiar? | `1.000.032` |
| 17 | ¿Cuántos registros tienen `activo` como verdadero después de normalizar? | `149.863` |
| 18 | ¿Cuántos registros tienen `activo` como falso después de normalizar? | `150.137` |
| 19 | ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? | `89.823` |
| 20 | ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? | `53.404` |
| 21 | ¿Cuántas personas nacieron antes de 1960? | `66.577` |
| 22 | ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)? | `140.134` |
| 23 | ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? | `187` |
| 24 | ¿Cuántos registros tienen nombre "Ana" y son "Medico"? | `172` |
| 25 | ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000? | `4.405` |
| 26 | ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980? | `3.241` |
| 27 | ¿Cuál es la ciudad con más "Ingenieros"? | `Popayan, 640 Ingenieros` |
| 28 | ¿Cuál es la profesión con el salario promedio más alto? | `Biologo, 807.351,86` |
| 29 | ¿Cuántos registros tienen email con dominio "gmail.com"? | `60.000` |
| 30 | ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? | `PENDIENTE` |

---

## Ejemplo de Solución

### Archivo `soluciones/02.py`

```python
import pandas as pd
import codecs

# Cargar datos
df = pd.read_csv('data/personas.csv')

# Descifrar nombres con ROT13
df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Contar cuántas veces aparece "Maria"
cantidad = df[df['nombre'] == 'Maria'].shape[0]

print(f"El nombre 'Maria' aparece {cantidad} veces")
```

### En el README, la solución se vería así:

| # | Ejercicio | Solución |
|---|-----------|----------|
| 02 | ¿Cuántas veces aparece el nombre "Maria" en el dataset? | `15234` |

*(El número 15234 es solo un ejemplo, debe calcular el valor real)*

---

## Comandos Útiles

```bash
# Ejecutar un script de solución
uv run python soluciones/01.py

# O si no usa uv
python soluciones/01.py
```

---

## Dependencias

El proyecto usa `pandas` y `matplotlib`. Si usa `uv`:

```bash
uv add pandas matplotlib
```

Si usa `pip`:

```bash
pip install pandas matplotlib
```
