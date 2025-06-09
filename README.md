# 🛍️ Tienda de Ropa 

Este proyecto consiste en una base de datos para una tienda de ropa, desarrollada con MongoDB. Contiene las colecciones necesarias para gestionar **usuarios, marcas, prendas y ventas**,.

## 📁 Estructura del Proyecto


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

