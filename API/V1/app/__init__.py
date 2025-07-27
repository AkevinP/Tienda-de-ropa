from flask import Flask
from app.controllers.marcas import marcas_bp
from app.controllers.prendas import prendas_bp
from app.controllers.usuarios import usuarios_bp
from app.controllers.ventas import ventas_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(marcas_bp, url_prefix="/api/v1/marcas")
app.register_blueprint(prendas_bp, url_prefix="/api/v1/prendas")
app.register_blueprint(usuarios_bp, url_prefix="/api/v1/usuarios")
app.register_blueprint(ventas_bp, url_prefix="/api/v1/ventas")
