from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.db import db

usuarios_bp = Blueprint("usuarios", __name__)
usuarios = db["usuarios"]

@usuarios_bp.route("", methods=["POST"])
def crear_usuario():
    data = request.get_json()
    nuevo = {
        "nombre": data["nombre"],
        "email": data["email"]
    }
    result = usuarios.insert_one(nuevo)
    nuevo["_id"] = str(result.inserted_id)
    return jsonify(nuevo), 201

@usuarios_bp.route("", methods=["GET"])
def listar_usuarios():
    resultado = list(usuarios.find())
    for u in resultado:
        u["_id"] = str(u["_id"])
    return jsonify(resultado)

@usuarios_bp.route("/<id>", methods=["GET"])
def obtener_usuario(id):
    usuario = usuarios.find_one({"_id": ObjectId(id)})
    if usuario:
        usuario["_id"] = str(usuario["_id"])
        return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

@usuarios_bp.route("/<id>", methods=["PUT"])
def actualizar_usuario(id):
    data = request.get_json()
    result = usuarios.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "nombre": data["nombre"],
            "email": data["email"]
        }}
    )
    if result.matched_count:
        return jsonify({"mensaje": "Usuario actualizado"})
    return jsonify({"error": "Usuario no encontrado"}), 404

@usuarios_bp.route("/<id>", methods=["DELETE"])
def eliminar_usuario(id):
    result = usuarios.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"mensaje": "Usuario eliminado"})
    return jsonify({"error": "Usuario no encontrado"}), 404

