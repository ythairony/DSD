from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()

bebidas = [
    {"item" : "Coca-cola", "valor" : "R$ 5,00"},
    {"item" : "Guarana", "valor" : "R$ 4,50"},
    {"item" : "Fanta", "valor" : "R$ 5,00"},
    {"item" : "Agua mineral", "valor" : "R$ 3,00"},
    {"item" : "Agua com gas", "valor" : "R$ 4,00"},
    {"item" : "Suco", "valor" : "R$ 6,00"},
    {"item" : "Del valle Kapo", "valor" : "R$ 3,00"},
    {"item" : "Cerveja", "valor" : "R$ 7,00"},
    {"item" : "Vodka", "valor" : "R$ 1,00"},
    {"item" : "Vinho", "valor" : "R$ 10,00"},
]


@app.get("/api/bebidas/get_all/")
def get_bebidas():
    return bebidas