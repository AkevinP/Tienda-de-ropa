# 🛍️ Tienda de Ropa — Base de Datos MongoDB

Este proyecto implementa una base de datos para una tienda de ropa, utilizando **MongoDB**. Está diseñada para administrar colecciones relacionadas con **clientes, productos, marcas y ventas**, todo desde un único script interactivo.

---

## 📁 Estructura del Proyecto

El repositorio contiene los siguientes archivos esenciales:

- `📜 tienda.js`: Contiene toda la lógica del script, incluyendo creación de colecciones, inserciones, consultas y operaciones CRUD.
- `🔐 .env`: Archivo de configuración que almacena de forma segura la URI de conexión a MongoDB Atlas. **(¡No se debe subir a GitHub!)**

---

## 🧩 Colecciones disponibles

El sistema cuenta con 4 colecciones bien diferenciadas:

- 👤 `usuarios`: Datos básicos de los clientes (nombre, correo electrónico).
- 👟 `marcas`: Información de marcas de ropa (nombre, país de origen).
- 👕 `prendas`: Productos disponibles en stock (nombre, marca, precio, unidades).
- 💸 `ventas`: Registro de ventas con relación directa a las prendas.

---

## 🔧 Operaciones implementadas

Cada colección incluye operaciones clave de manipulación y consulta:

- ✅ Inserción de uno o múltiples documentos
- 🔁 Actualización de campos
- 🗑️ Eliminación de registros
- 📊 Consultas especializadas:

  - Total vendido por prenda en una fecha específica
  - Listado de marcas con al menos una venta
  - Cálculo de stock restante por prenda
  - Ranking de las 5 marcas más vendidas

---

## 🧪 Ejemplo de documento en cada colección

### 👤 usuarios
```json
{
  "nombre": "Ana",
  "email": "ana@mail.com"
}
```
## 🚀 ¿Cómo ejecutar el proyecto?
1.Cloná el repositorio
2.Instalá las dependencias:

*bash
*npm install
*Configurá tu archivo .env con la URI de MongoDB Atlas

3.Ejecutá el script:
bash
node tienda.js

## 🚀 Tecnologías utilizadas

- Python 3
- Flask
- MongoDB (via PyMongo)
- Postman (para pruebas)
- dotenv (para variables de entorno)


## ⚙️ Instalación

1. Clona el repositorio:
   git clone https://github.com/tu-usuario/tiendaderopa.git
   cd tiendaderopa/API/V1

2. Crea y activa un entorno virtual:
   python -m venv .venv
   .venv\Scripts\activate  # En Windows

3. Instala dependencias:
   pip install -r requirements.txt

4. Configura tu archivo `.env`:
   MONGODB_URI=mongodb://localhost:27017

5. Ejecuta el servidor:
   python run.py

## 📮 Endpoints disponibles

### Usuarios
- GET /api/v1/usuarios
- POST /api/v1/usuarios
- PUT /api/v1/usuarios/<id>
- DELETE /api/v1/usuarios/<id>

### Marcas
- GET /api/v1/marcas
- POST /api/v1/marcas
- PUT /api/v1/marcas/<id>
- DELETE /api/v1/marcas/<id>

### Prendas
- GET /api/v1/prendas
- POST /api/v1/prendas
- PUT /api/v1/prendas/<id>
- DELETE /api/v1/prendas/<id>

### Ventas
- GET /api/v1/ventas
- POST /api/v1/ventas
- PUT /api/v1/ventas/<id>
- DELETE /api/v1/ventas/<id>

## 🧪 Pruebas con Postman

1. Abre Postman y crea una colección llamada Tienda de Ropa
2. Agrega las solicitudes con sus respectivos métodos y URLs





