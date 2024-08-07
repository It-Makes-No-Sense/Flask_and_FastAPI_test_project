from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    order_date = Column(DateTime, default=datetime.now())
    status = Column(String)

    user = relationship("User", back_populates="orders")
    item = relationship("Item", back_populates="orders")


User.orders = relationship("Order", back_populates="user")
Item.orders = relationship("Order", back_populates="item")


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: bytes


class ItemCreate(BaseModel):
    name: str
    description: str
    price: int


class OrderCreate(BaseModel):
    user_id: int
    item_id: int
    status: str


class OrderUpdate(BaseModel):
    order_id: int
    status: str
