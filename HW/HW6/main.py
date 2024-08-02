from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import database
import crud
import models

app = FastAPI()


# Создание подключения к базе данных при запуске приложения
@app.on_event("startup")
async def startup():
    database.Base.metadata.create_all(bind=database.engine)


# Функция для получения сессии базы данных
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_class=RedirectResponse, status_code=302)
async def root():
    return '/docs'


# CRUD операции для пользователей
@app.post("/users/")
async def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users")
async def users(db: Session = Depends(get_db)):
    user_list = crud.get_users(db)
    return user_list


@app.get("/users/{user_id}/")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}/")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


# CRUD операции для товаров
@app.post("/items/")
async def create_item(item: models.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@app.get("/items/{item_id}/")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}/")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db, item_id)


# CRUD операции для заказов
@app.post("/orders/")
async def create_order(order: models.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@app.get("/orders/{order_id}/")
async def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.delete("/orders/{order_id}/")
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    return crud.delete_order(db, order_id)
