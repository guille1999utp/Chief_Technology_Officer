from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String
from database.session import meta, engine

# creamos tabla Characters y la inicializamos cuando la aplicacion arranque la creamos
Character = Table(
    "characters",
    meta,
    Column("id",Integer, primary_key=True, index=True),Column("name",String(100)) ,
    Column("status",String(50)),
    Column("species",String(50)),
    Column("gender",String(20)))

meta.create_all(engine)