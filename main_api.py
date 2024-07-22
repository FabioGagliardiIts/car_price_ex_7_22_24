from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
from db import db

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/db/{collection_id}")
async def create_collection(collection_id: str):
    collection = db.connect_collection(collection_id)
    collection.close()
    return {"result": 'ok'}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    print(f"{item_id} {q}")
    return {"result": 'ok'}


@app.post("/items")
async def create_item(item: Item):
    print(item.name)
    print(item.description)
    print(item.price)
    print(item.tax)
    print("\n")
    return {"result": 'ok'}
