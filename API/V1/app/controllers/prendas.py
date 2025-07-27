from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.db import db

prendas_bp = Blueprint("prendas", __name__)
prendas = db["prendas"]

@prendas_bp.route("", methods=["POST"])
def crear_prenda():
    data = request.get_json()
    nueva = {
        "nombre": data["nombre"],
        "talla": data["talla"],
        "color": data["color"],
        "precio": data["precio"],
        "marca_id": ObjectId(data["marca_id"])
    }
    result = prendas.insert_one(nueva)
    nueva["_id"] = str(result.inserted_id)
    nueva["marca_id"] = str(nueva["marca_id"])
    return jsonify(nueva), 201

@prendas_bp.route("", methods=["GET"])
def listar_prendas():
    resultado = list(prendas.find())
    for p in resultado:
        p["_id"] = str(p["_id"])
        p["marca_id"] = str(p["marca_id"])
    return jsonify(resultado)

@prendas_bp.route("/<id>", methods=["GET"])
def obtener_prenda(id):
    prenda = prendas.find_one({"_id": ObjectId(id)})
    if prenda:
        prenda["_id"] = str(prenda["_id"])
        prenda["marca_id"] = str(prenda["marca_id"])
        return jsonify(prenda)
    return jsonify({"error": "Prenda no encontrada"}), 404

@prendas_bp.route("/<id>", methods=["PUT"])
def actualizar_prenda(id):
    data = request.get_json()
    result = prendas.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "nombre": data["nombre"],
            "talla": data["talla"],
            "color": data["color"],
            "precio": data["precio"],
            "marca_id": ObjectId(data["marca_id"])
        }}
    )
    if result.matched_count:
        return jsonify({"mensaje": "Prenda actualizada"})
    return jsonify({"error": "Prenda no encontrada"}), 404

@prendas_bp.route("/<id>", methods=["DELETE"])
def eliminar_prenda(id):
    result = prendas.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"mensaje": "Prenda eliminada"})
    return jsonify({"error": "Prenda no encontrada"}), 404
