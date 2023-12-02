# from typing import Union
# import requests
# from fastapi import FastAPI

# app = FastAPI()



# @app.get("/gateway/lanches/")
# def get_lanches():
#     response = requests.get("http://localhost:20000/api/lanches/get_all/")
#     # response = requests.get("http://localhost:20000/api/lanches/get_all/") #Trocar localhost pelo IP do IPConfig
#     return response.json()


# @app.get("/gateway/bebidas/")
# def get_bebidas():
#     response = requests.get("http://localhost:30000/api/bebidas/get_all/")
#     return response.json()


# @app.get("/gateway/doces/")
# def get_doces():
#     response = requests.get("http://localhost:40000/api/doces/get_all/")
#     return response.json()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Configuração do CORS permitindo todas as origens para desenvolvimento
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode restringir para o seu domínio quando estiver em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/gateway/lanches/")
def get_lanches():
    response = requests.get("http://localhost:20000/api/lanches/get_all/")
    return response.json()

@app.get("/gateway/bebidas/")
def get_bebidas():
    response = requests.get("http://localhost:30000/api/bebidas/get_all/")
    return response.json()

@app.get("/gateway/doces/")
def get_doces():
    response = requests.get("http://localhost:40000/api/doces/get_all/")
    return response.json()
