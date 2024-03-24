FROM python:3.9

WORKDIR /app

# importamos paquetes necesarios para que corra la aplicacion
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto excepto las variables de entornos de prueba
COPY --exclude .env . .

# asignamos el puerto de la aplicacion
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]