from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url")
async def url():
    return {"message": "Hello World from URL"}



# Entidad usuario

class User(BaseModel):
    id: int
    nombre: str
    email: str
    usuario: str
    rol: str



@app.get("/usersclass")
async def get_users_class():
    return [User(id=1, nombre="Carlos Mendoza", email="carlos@gmail.com", usuario="cmendoza", rol="administrador")]








@app.get("/users")
async def get_users():
    return [

            {
                "id": 1,
                "nombre": "Carlos Mendoza",
                "email": "carlos.mendoza@example.com",
                "usuario": "cmendoza",
                "rol": "administrador"
            },
            {
                "id": 2,
                "nombre": "Lucía Torres",
                "email": "lucia.torres@example.com",
                "usuario": "ltorres",
                "rol": "editor"
            },
            {
                "id": 3,
                "nombre": "Javier López",
                "email": "javier.lopez@example.com",
                "usuario": "jlopez",
                "rol": "usuario"
            },
            {
                "id": 4,
                "nombre": "Ana Castillo",
                "email": "ana.castillo@example.com",
                "usuario": "acastillo",
                "rol": "moderador"
            },
            {
                "id": 5,
                "nombre": "Miguel Ruiz",
                "email": "miguel.ruiz@example.com",
                "usuario": "mruiz",
                "rol": "usuario"
            }
        ]