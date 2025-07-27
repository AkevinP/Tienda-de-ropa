from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["tiendaRopa"]

usuarios = db["usuarios"]
marcas = db["marcas"]
prendas = db["prendas"]
ventas = db["ventas"]
