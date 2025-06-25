# 🛍️ Tienda de Ropa 

Este proyecto consiste en una base de datos para una tienda de ropa, desarrollada con MongoDB. Contiene las colecciones necesarias para gestionar **usuarios, marcas, prendas y ventas**.

## 📁 Estructura del Proyecto

En su estructura contamos con 2  archivos importantes los cuales son:

1. Tienda.js= Con el cual se logra ver la estructura de la programación con la que se realizo.
2. Env= Este archivo es la ruta con la cual se dirige hacia Mongodb Compass.

## 🧩 Colecciones

Se han implementado las siguientes colecciones:

- **👤usuarios**: Información básica de los clientes.
- **✅marcas**: Marcas de ropa disponibles.
- **👕prendas**: Productos de ropa en stock.
- **💸ventas**: Registro de ventas realizadas.

## 🔧 Operaciones Incluidas

Cada colección tiene implementadas las siguientes operaciones:

1. Insertar un dato
2. Insertar varios datos
3. Actualizar un dato
4. Eliminar datos

Además, el proyecto incluye las siguientes consultas:

- Obtener la cantidad vendida de prendas por fecha.
- Listar las marcas que han registrado al menos una venta.
- Mostrar prendas vendidas y su stock restante.
- Mostrar el top 5 de marcas más vendidas.

## 🧪 Ejemplos JSON de cada colección

### usuarios
```json
{
  "nombre": "Ana",
  "email": "ana@mail.com"

// Cantidad vendida por prenda en 2025-06-01
ventas.aggregate([
  { $match: { fechaVenta: { $gte: ..., $lt: ... } } },
  { $group: { _id: '$prendaId', totalVendido: { $sum: '$cantidad' } } }
]);

// Top 5 marcas más vendidas
ventas.aggregate([
  { $lookup: { from: 'prendas', localField: 'prendaId', foreignField: '_id', as: 'prenda' } },
  { $unwind: '$prenda' },
  { $group: { _id: '$prenda.marca', totalVentas: { $sum: '$cantidad' } } },
  { $sort: { totalVentas: -1 } },
  { $limit: 5 }
]);

