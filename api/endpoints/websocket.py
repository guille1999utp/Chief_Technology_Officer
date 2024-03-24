from fastapi import WebSocket, APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from api.models.character import Character
import json
import asyncio

router = APIRouter()

# WebSocket Endpoint para obtener los datos de los personajes
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    try:
        while True:
            characters = db.query(Character).all()  

            characters_dict = [
                {
                    "id": char.id,
                    "name": char.name,
                    "status": char.status,
                    "species": char.species,
                    "gender": char.gender
                }
                for char in characters
            ]

            await websocket.send_text(json.dumps(characters_dict))

            await asyncio.sleep(1)
    except Exception as e:
        print(f"Error en WebSocket: {e}")
        await websocket.close()