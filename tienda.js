const { MongoClient, ObjectId } = require('mongodb');
const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri);

async function main() {
  try {
    await client.connect();
    const db = client.db('tiendaRopa');

    // Colecciones
    const usuarios = db.collection('usuarios');
    const marcas = db.collection('marcas');
    const prendas = db.collection('prendas');
    const ventas = db.collection('ventas');

    // Limpio colecciones para pruebas
    await usuarios.deleteMany({});
    await marcas.deleteMany({});
    await prendas.deleteMany({});
    await ventas.deleteMany({});

    // Insertar datos ficticios
    await usuarios.insertMany([
      { nombre: 'Ana', email: 'ana@mail.com' },
      { nombre: 'Luis', email: 'luis@mail.com' }
    ]);

    await marcas.insertMany([
      { nombre: 'Nike', pais: 'EEUU' },
      { nombre: 'Adidas', pais: 'Alemania' },
      { nombre: 'Puma', pais: 'Alemania' }
    ]);

    // Insertar prendas con referencia a marca por nombre (para simplificar)
    await prendas.insertMany([
      { nombre: 'Camiseta', marca: 'Nike', stock: 50, precio: 20 },
      { nombre: 'Pantalón', marca: 'Adidas', stock: 30, precio: 40 },
      { nombre: 'Zapatillas', marca: 'Puma', stock: 20, precio: 60 }
    ]);

    // Insertar ventas, referenciando prendas por su _id
    const camiseta = await prendas.findOne({ nombre: 'Camiseta' });
    const pantalon = await prendas.findOne({ nombre: 'Pantalón' });
    const zapatillas = await prendas.findOne({ nombre: 'Zapatillas' });

    await ventas.insertMany([
      { prendaId: camiseta._id, cantidad: 5, fechaVenta: new Date('2025-06-01') },
      { prendaId: pantalon._id, cantidad: 3, fechaVenta: new Date('2025-06-01') },
      { prendaId: zapatillas._id, cantidad: 2, fechaVenta: new Date('2025-06-02') },
      { prendaId: camiseta._id, cantidad: 4, fechaVenta: new Date('2025-06-03') }
    ]);

    // --- OPERACIONES CRUD EJEMPLO ---

    // Actualizar email de usuario Ana
    await usuarios.updateOne({ nombre: 'Ana' }, { $set: { email: 'ana.actualizada@mail.com' } });

    // Eliminar la marca Puma (ejemplo)
    await marcas.deleteOne({ nombre: 'Puma' });

    // --- CONSULTAS ---

    // i) Cantidad vendida de prendas en una fecha específica
    // Comentario: suma total de prendas vendidas en 2025-06-01 agrupadas por prenda
    const fechaConsulta = new Date('2025-06-01');
    const ventasPorFecha = await ventas.aggregate([
      { $match: { fechaVenta: { $gte: new Date(fechaConsulta.setHours(0,0,0,0)), $lt: new Date(fechaConsulta.setHours(23,59,59,999)) } } },
      { $group: { _id: '$prendaId', totalVendido: { $sum: '$cantidad' } } }
    ]).toArray();

    // Mostrar resultados con nombre de prenda
    console.log('\nCantidad vendida por prenda en 2025-06-01:');
    for (const venta of ventasPorFecha) {
      const prenda = await prendas.findOne({ _id: venta._id });
      console.log(`- ${prenda.nombre}: ${venta.totalVendido} unidades`);
    }

    // ii) Lista de marcas con al menos una venta
    // Comentario: buscar marcas que tengan alguna venta
    const marcasConVentas = await ventas.aggregate([
      {
        $lookup: {
          from: 'prendas',
          localField: 'prendaId',
          foreignField: '_id',
          as: 'prenda'
        }
      },
      { $unwind: '$prenda' },
      { $group: { _id: '$prenda.marca' } }
    ]).toArray();

    console.log('\nMarcas con al menos una venta:');
    marcasConVentas.forEach(m => console.log('- ' + m._id));

    // iii) Prendas vendidas y cantidad restante en stock
    // Comentario: suma total vendida por prenda y calcular stock restante
    const prendasVendidas = await ventas.aggregate([
      { $group: { _id: '$prendaId', totalVendido: { $sum: '$cantidad' } } }
    ]).toArray();

    console.log('\nPrendas vendidas y stock restante:');
    for (const pv of prendasVendidas) {
      const prenda = await prendas.findOne({ _id: pv._id });
      console.log(`- ${prenda.nombre}: Vendidas = ${pv.totalVendido}, Stock restante = ${prenda.stock - pv.totalVendido}`);
    }

    // iv) Listado de las 5 marcas más vendidas y su cantidad de ventas
    // Comentario: sumar ventas agrupadas por marca y ordenar descendente
    const topMarcas = await ventas.aggregate([
      {
        $lookup: {
          from: 'prendas',
          localField: 'prendaId',
          foreignField: '_id',
          as: 'prenda'
        }
      },
      { $unwind: '$prenda' },
      {
        $group: {
          _id: '$prenda.marca',
          totalVentas: { $sum: '$cantidad' }
        }
      },
      { $sort: { totalVentas: -1 } },
      { $limit: 5 }
    ]).toArray();

    console.log('\nTop 5 marcas más vendidas:');
    topMarcas.forEach(m => {
      console.log(`- ${m._id}: ${m.totalVentas} ventas`);
    });

  } catch (e) {
    console.error(e);
  } finally {
    await client.close();
  }
}

main();
