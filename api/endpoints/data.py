from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from utils.fetch_data import get_all_character
from api.models.character import Character 

router = APIRouter()

# API Endpoints

# obtiene todos los datos de los personajes de rick y morty
@router.get("/api/data/")
def get_all_data():
    data = get_all_character()
    return data

# Almacena los datos de los personajes de Rick y Morty en la base de datos y retornamos los datos guardados
@router.post("/api/data/")
def store_data(db: Session = Depends(get_db)):
    data = get_all_character()

    characters = data["results"]
    for character in characters:
        # Utiliza la tabla Character directamente
        db.execute(
            Character.insert().values(
                name=character["name"],
                status=character["status"],
                species=character["species"],
                gender=character["gender"]
            )
        )
    db.commit()

    return characters

# Obtiene los datos de un personaje específico de Rick y Morty
@router.get("/api/data/{data_id}")
def read_data(data_id: int, db: Session = Depends(get_db)):
    # Consulta la base de datos para obtener el personaje con el ID proporcionado
    character = db.execute(
        Character.select().where(Character.c.id == data_id)
    ).fetchone()

    if character is None:
        # Si no se encuentra ningún personaje con el ID proporcionado, devuelve un error 404
        raise HTTPException(status_code=404, detail="El personaje no fue encontrado")

    # Crea un diccionario con los datos del personaje y devuelve la respuesta
    character_dict = {
        "id": character[0],  # el primer elemento es el ID
        "name": character[1],  # el segundo elemento es el nombre
        "status": character[2],  # el tercer elemento es el estado
        "species": character[3],  # el cuarto elemento es la especie
        "gender": character[4]  # el quinto elemento es el género
    }
    return character_dict