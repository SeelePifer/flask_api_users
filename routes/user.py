from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id== id)).fetchall()

@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(users.c.name,
    users.c.email,
    users.c.password,
    users.c.role)).fetchall()

    return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def read_data(id:int, user:User):
    conn.execute(users.update().where(users.c.id==id).values(users.c.name,
    users.c.email,
    users.c.password,
    users.c.role)).fetchall()
    return conn.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_data(id:int):
    conn.execute(users.delete().where(users.c.id==id)).fetchall()
    return conn.execute(users.select()).fetchall()
