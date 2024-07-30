import databases
import sqlalchemy
from sqlalchemy import MetaData, Table, Column, create_engine
from datetime import date

DATABASE_URL = "sqlite:///my_db.db"

database = databases.Database(DATABASE_URL)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True),
    Column("name", sqlalchemy.String()),
    Column("surname", sqlalchemy.String()),
    Column("email", sqlalchemy.String()),
    Column("password", sqlalchemy.String()),
)

items = Table(
    "items",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True),
    Column("name", sqlalchemy.String(150)),
    Column("description", sqlalchemy.String(500)),
    Column("price", sqlalchemy.Float(2)),
)

orders = Table(
    "orders",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True),
    Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
           nullable=False),
    Column("item_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id'),
           nullable=False),
    Column("order_date", sqlalchemy.Date, default=date.today()),
    Column("status", sqlalchemy.String, default="Создан"),
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
