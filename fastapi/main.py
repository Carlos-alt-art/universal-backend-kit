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




users_list = [
    User(id=1, nombre="Carlos Mendoza", email="carlos@gmail.com", usuario="cmendoza", rol="administrador"),
    User(id=2, nombre="Lucía Torres", email="lucia@gmail.com", usuario="ltorres", rol="editor"),
    User(id=3, nombre="Javier López", email="javier@gmai.com", usuario="jlopez", rol="usuario"),
    User(id=4, nombre="Ana Castillo", email="ana@gmail.com", usuario="acastillo", rol="moderador")
]


@app.get("/users")
async def get_users_class():
    return users_list


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.get("/userslambda/{user_id}")
async def get_user(user_id: int):
    users = filter(lambda user: user.id == user_id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}
    







@app.get("/usersjson")
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




@app.post("/users/")
async def user(user: User):
    users_list.append(user)



@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for saved_user in users_list:
        if saved_user.id == user_id:
            saved_user.nombre = user.nombre
            saved_user.email = user.email
            saved_user.usuario = user.usuario
            saved_user.rol = user.rol
            return {"message": "User updated successfully"}
        


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, user: User):
    for delete_user in users_list:
        if delete_user.id == user_id:
            users_list.remove(delete_user)
            return {"message": "User updated successfully"} 