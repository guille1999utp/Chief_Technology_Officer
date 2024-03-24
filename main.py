from fastapi import FastAPI
from api.endpoints import data, websocket

#creacion de app con Fastapi
app = FastAPI()

# importamos  las rutas y el websocket
app.include_router(data.router)
app.include_router(websocket.router)