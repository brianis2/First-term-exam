from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel
from typing import Optional

app = FastAPI()



class User(SQLModel):
    id: int
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

class UserCreate(SQLModel):
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

class UserUpdate(SQLModel):
    username: str
    email: Optional[str] = None
    is_active: bool = True

class LoginData(SQLModel):
    username: str
    password: str



db_users = [
    User(id=1, username="admin", password="admin", email="admin@test.com", is_active=True)
]



@app.get("/")
def root():
    return {"mensaje": "API funcionando"}



@app.get("/users")
def get_users():
    return db_users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in db_users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/users")
def create_user(new_user: UserCreate):
  
    for user in db_users:
        if user.username == new_user.username:
            raise HTTPException(status_code=400, detail="Username ya existe")

    new_id = max(user.id for user in db_users) + 1 if db_users else 1

    user = User(
        id=new_id,
        username=new_user.username,
        password=new_user.password,
        email=new_user.email,
        is_active=new_user.is_active
    )

    db_users.append(user)
    return {"message": "Usuario creado", "user": user}


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_data: UserUpdate):
    for user in db_users:
        if user.id == user_id:
            user.username = updated_data.username
            user.email = updated_data.email
            user.is_active = updated_data.is_active
            return {"message": "Usuario actualizado", "user": user}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(db_users):
        if user.id == user_id:
            deleted = db_users.pop(i)
            return {"message": "Usuario eliminado", "user": deleted}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/login")
def login(user_login: LoginData):
    for user in db_users:
        if user.username == user_login.username and user.password == user_login.password:
            return {"status": "success", "message": f"Bienvenido {user.username}"}

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
