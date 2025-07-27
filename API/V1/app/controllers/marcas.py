from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.db import db

marcas_bp = Blueprint("marcas", __name__)
marcas = db["marcas"]

@marcas_bp.route("", methods=["POST"])
def crear_marca():
    data = request.get_json()
    nueva = {
        "nombre": data["nombre"]
    }
    result = marcas.insert_one(nueva)
    nueva["_id"] = str(result.inserted_id)
    return jsonify(nueva), 201

@marcas_bp.route("", methods=["GET"])
def listar_marcas():
    resultado = list(marcas.find())
    for m in resultado:
        m["_id"] = str(m["_id"])
    return jsonify(resultado)

@marcas_bp.route("/<id>", methods=["GET"])
def obtener_marca(id):
    marca = marcas.find_one({"_id": ObjectId(id)})
    if marca:
        marca["_id"] = str(marca["_id"])
        return jsonify(marca)
    return jsonify({"error": "Marca no encontrada"}), 404

@marcas_bp.route("/<id>", methods=["PUT"])
def actualizar_marca(id):
    data = request.get_json()
    result = marcas.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"nombre": data["nombre"]}}
    )
    if result.matched_count:
        return jsonify({"mensaje": "Marca actualizada"})
    return jsonify({"error": "Marca no encontrada"}), 404

@marcas_bp.route("/<id>", methods=["DELETE"])
def eliminar_marca(id):
    result = marcas.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"mensaje": "Marca eliminada"})
    return jsonify({"error": "Marca no encontrada"}), 404
