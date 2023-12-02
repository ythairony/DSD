from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()

lanches = [
    {"item" : "Pizza", "valor" : "R$ 40,00"},
    {"item" : "Cachorro Quente", "valor" : "R$ 8,00"},
    {"item" : "Hamburger", "valor" : "R$ 15,00"},
    {"item" : "Kalzone", "valor" : "R$ 9,00"},
    {"item" : "Esfirra", "valor" : "R$ 2,00"},
    {"item" : "Sanduiche", "valor" : "R$ 12,00"},
    {"item" : "Batata Frita", "valor" : "R$ 13,00"},
    {"item" : "Coxinha", "valor" : "R$ 3,00"},
    {"item" : "Pastel", "valor" : "R$ 5,00"},
    {"item" : "Empada", "valor" : "R$ 3,00"},
]


@app.get("/api/lanches/get_all/")
def get_lanches():
    return lanches
