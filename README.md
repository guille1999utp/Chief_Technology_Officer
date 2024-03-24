
# Documentación de Endpoints - Proyecto aquinasnetwork

## Descripción del Proyecto

Esta aplicación permite consultar la API de Rick and Morty para obtener información sobre los personajes, almacenarlos en una base de datos local y buscar personajes a través de WebSockets.

### Pasos para Usar Localmente

1. clonar el proyecto con el siguiente comando: `git clone https://github.com/guille1999utp/Chief_Technology_Officer.git`

2. nos ubicamos dentro del proyecto: `cd Chief_Technology_Officer`

3. Instalamos las dependencias del proyecto con el siguiente comando (se debe tener instalado python y pip):

```console
 pip install -r requirements.txt
```

4. Inicia el servidor con el siguiente comando en la misma ruta: 

```console
 uvicorn main:app --reload
```

2. Configuración de Variables de Entorno

Crea un archivo llamado .env en la raíz del proyecto con la siguiente estructura:

```console
    MYSQL_USER = guille1999
    MYSQL_PASSWORD = prueba-tecnica
    MYSQL_HOST = localhost
    MYSQL_PORT = 3306
    MYSQL_DATABASE = aquinasnetwork
```

3. Creación de la Base de Datos con docker

para crear la base de matos de manera local debemos tener instalado docker en este, luego corremos el siguiente comando para correr la imagen de mysql:

```console
  docker compose up mysql
```

### Pasos para Usar Localmente con docker

1. nos ubicaos en nuestro archivo raiz y ejecutamos el siguiente comando

```console
  docker compose up --build
```

### Enpoints

Las API para probar son con ruta base (http://127.0.0.1:8000):

- `GET /api/data/`: Obtiene todos los personajes de rick y morty.
- `POST /api/data/`: obtiene todos los personajes de rick y morty y los guarda en la base de datos.
- `GET /api/data/{number}`: Obtiene personaje por id.\

Para la conexion websocket se utiliza como base la siguiente ruta (ws://localhost:8000/ws):
- `WS /ws`: realiza conexion WebSocket con nuestro servidor.

### Swagger de FastApi

Si quieres ver más información sobre los endpoints disponibles, ingresa a la siguiente ruta: [http://localhost:8000/docs](http://localhost:8000/docs)