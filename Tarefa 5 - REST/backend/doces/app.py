from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()

doces = [
    {"item" : "Brigadeiro", "valor" : "R$ 2,00"},
    {"item" : "Beijinho", "valor" : "R$ 2,00"},
    {"item" : "Bem Casado", "valor" : "R$ 2,00"},
    {"item" : "Romeu e Julieta", "valor" : "R$ 3,00"},
    {"item" : "Sorvete", "valor" : "R$ 4,00"},
    {"item" : "Picole", "valor" : "R$ 4,00"},
    {"item" : "Chocolate", "valor" : "R$ 6,00"},
    {"item" : "Brownie", "valor" : "R$ 7,00"},
    {"item" : "Cookie", "valor" : "R$ 6,00"},
    {"item" : "Doce com Nutella", "valor" : "R$ 10,00"},
]


@app.get("/api/doces/get_all/")
def get_doces():
    return doces