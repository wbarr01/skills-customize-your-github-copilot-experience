from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

items: List[Item] = []

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app"}
