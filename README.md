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
👟 marcas
{
  "nombre": "Nike",
  "pais": "EEUU"
}

👕 prendas
{
  "nombre": "Camiseta",
  "marca": "Nike",
  "stock": 50,
  "precio": 20
}
💸 ventas
{
  "prendaId": "ObjectId(...)",
  "cantidad": 5,
  "fechaVenta": "2025-06-01"
}

🚀 ¿Cómo ejecutar el proyecto?
Cloná el repositorio

Instalá las dependencias:

bash
npm install
Configurá tu archivo .env con la URI de MongoDB Atlas

Ejecutá el script:

bash
node tienda.js


Una vez pegado todo, guardás el archivo ¡y listo! Ya tenés un `README.md` claro, vistoso y listo para compartir tu proyecto con el mundo. ¿Querés que también le agregue una sección opcional de “Mejoras futuras” o “Contribuciones”?


