from pydantic import BaseModel, Field, EmailStr
from datetime import date


# Таблица товаров должна содержать следующие поля:
# id (PRIMARY KEY), название, описание и цена.
class Item(BaseModel):
    item_id: int
    name: str = Field(max_length=150)
    description: str = Field(max_length=500)
    price: float


class ItemIn(BaseModel):
    name: str = Field(max_length=150)
    description: str = Field(max_length=500)
    price: float


# Таблица пользователей должна содержать следующие поля:
# id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
class User(BaseModel):
    user_id: int
    name: str
    surname: str
    email: str = EmailStr()
    password: str = Field(min_length=5)


class UserIn(BaseModel):
    name: str
    surname: str
    email: str = EmailStr()
    password: str = Field(min_length=5)


# Таблица заказов должна содержать следующие поля:
# id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
class Order(BaseModel):
    order_id: int
    user_id: int
    item_id: int
    order_date: date
    status: str


class OrderIn(BaseModel):
    user_id: int
    item_id: int
    order_date: date
    status: str
