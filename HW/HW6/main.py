from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from schema import users, items, orders, database
from models import Item, User, Order, ItemIn, UserIn, OrderIn
from typing import List

app = FastAPI()


@app.get("/", response_class=RedirectResponse, status_code=302)
async def root():
    return '/docs'


@app.get('/users', response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/user/{id}', response_model=User)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/user', response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(
        **user.dict()
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.put('/user/{id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete('/user/{id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f"User {user_id} deleted"}
