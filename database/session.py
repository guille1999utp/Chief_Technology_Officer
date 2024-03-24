
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Importa la configuración de la base de datos desde el módulo core.config
from core.config import settings

# Obtiene la URL de la base de datos de la configuración
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

# Crea un motor de base de datos utilizando la URL de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Esta clase se utiliza para instanciar sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Realiza la conexión inicial a la base de datos utilizando el motor creado
engine.connect()

# Crea un objeto MetaData para almacenar información sobre la estructura de la base de datos
meta = MetaData()

# Define una función llamada get_db() que se utiliza para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
