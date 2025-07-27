from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.db import db

ventas_bp = Blueprint("ventas", __name__)
ventas = db["ventas"]

@ventas_bp.route("", methods=["POST"])
def crear_venta():
    data = request.get_json()
    nueva = {
        "usuario_id": ObjectId(data["usuario_id"]),
        "prenda_id": ObjectId(data["prenda_id"]),
        "fecha": data["fecha"],
        "cantidad": data["cantidad"],
        "total": data["total"]
    }
    result = ventas.insert_one(nueva)
    nueva["_id"] = str(result.inserted_id)
    nueva["usuario_id"] = str(nueva["usuario_id"])
    nueva["prenda_id"] = str(nueva["prenda_id"])
    return jsonify(nueva), 201

@ventas_bp.route("", methods=["GET"])
def listar_ventas():
    resultado = list(ventas.find())
    for v in resultado:
        v["_id"] = str(v["_id"])
        v["usuario_id"] = str(v["usuario_id"])
        v["prenda_id"] = str(v["prenda_id"])
    return jsonify(resultado)

@ventas_bp.route("/<id>", methods=["GET"])
def obtener_venta(id):
    venta = ventas.find_one({"_id": ObjectId(id)})
    if venta:
        venta["_id"] = str(venta["_id"])
        venta["usuario_id"] = str(venta["usuario_id"])
        venta["prenda_id"] = str(venta["prenda_id"])
        return jsonify(venta)
    return jsonify({"error": "Venta no encontrada"}), 404

@ventas_bp.route("/<id>", methods=["PUT"])
def actualizar_venta(id):
    data = request.get_json()
    result = ventas.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "usuario_id": ObjectId(data["usuario_id"]),
            "prenda_id": ObjectId(data["prenda_id"]),
            "fecha": data["fecha"],
            "cantidad": data["cantidad"],
            "total": data["total"]
        }}
    )
    if result.matched_count:
        return jsonify({"mensaje": "Venta actualizada"})
    return jsonify({"error": "Venta no encontrada"}), 404

@ventas_bp.route("/<id>", methods=["DELETE"])
def eliminar_venta(id):
    result = ventas.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"mensaje": "Venta eliminada"})
    return jsonify({"error": "Venta no encontrada"}), 404
