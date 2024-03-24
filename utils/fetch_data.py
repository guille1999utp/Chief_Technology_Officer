import requests
from fastapi import HTTPException

# api de rick y morty para obtener personajes
def get_all_character():
    response = requests.get("https://rickandmortyapi.com/api/character")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="No se pudieron obtener los datos del servicio externo")
    return response.json()