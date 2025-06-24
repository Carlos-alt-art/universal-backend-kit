


Tipado de variables, a paritr del python 3.6

A partir de esta vesrión de python se pude tipar las variebales, es un tipado debil

mas rapido, mas claro





# Guía de configuración FastAPI

## 🐍 1. **Crea un entorno virtual**

Desde la terminal, en la carpeta de tu proyecto:

```bash
python -m venv venv
```

Esto creará una carpeta `venv/` que contendrá un Python aislado solo para tu proyecto.

## ⚙️ 2. **Activa el entorno virtual**

**En Windows:**

```bash
venv\Scripts\activate
```

**En macOS / Linux:**

```bash
source venv/bin/activate
```

Cuando está activado, deberías ver algo así en la terminal:

```bash
(venv) $
```

## 📦 3. **Instala FastAPI y Uvicorn**

Con el entorno activado, instala las dependencias base:

```bash
pip install fastapi uvicorn[standard]
```

`uvicorn[standard]` incluye mejoras como soporte para `watchdog`, `httptools`, etc.

## 📄 4. **Guarda los paquetes en `requirements.txt`**

```bash
pip freeze > requirements.txt
```

Así podrás replicar el entorno en otros equipos o contenedores fácilmente.

## 🚀 5. **Ejecuta tu app FastAPI**

Crea un archivo básico como `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "¡Hola desde FastAPI!"}
```

Ejecuta el servidor:

```bash
fastapi dev main.py
```

Abre en tu navegador:

```bash
http://localhost:8000
```

Y la documentación automática en:

``` bash
http://localhost:8000/docs #Documentación con Swagger

http://localhost:8000/redoc #Documentación con Redocly
```