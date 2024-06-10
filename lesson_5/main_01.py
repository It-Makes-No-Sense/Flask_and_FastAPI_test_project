from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging

from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="./lesson_5/templates")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Пример с HTMl
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


# Пример с JSONResponse
@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)

# Пример с шаблоном html

@app.get('/{name}', response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "name": name})


@app.get("/items/{item_id}")  # /items/42?q=text -> q = 'text'
async def read_item(item_id: int, q: str = None):
    logger.info('Отработал GET запрос.')
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    # curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept:application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best","price": 9.99, "tax": 0.99}'
    logger.info('Отработал POST запрос.')
    return item


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    # curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept:application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of theobject", "price": 77.7, "tax": 10.01}'
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    # curl -X 'DELETE' 'http://127.0.0.1:8000/items/13' -H 'accept:application/json'
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}
