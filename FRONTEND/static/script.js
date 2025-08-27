document.addEventListener('DOMContentLoaded', () => {
  cargarMarcas();               // ✅ llena el combo de marcas
  cargarMarcasConVentas();
  cargarPrendasVendidas();
  cargarTopMarcas();
});

function cargarMarcas() {
  fetch('/api/v1/marcas')
    .then(res => res.json())
    .then(data => {
      const select = document.getElementById('marca_id');
      select.innerHTML = '';
      data.forEach(marca => {
        const option = document.createElement('option');
        option.value = marca.id;
        option.textContent = marca.nombre;
        select.appendChild(option);
      });
    });
}

function cargarMarcasConVentas() {
  fetch('/api/v1/marcas_con_ventas')
    .then(res => res.json())
    .then(data => {
      const tabla = document.getElementById('tabla-marcas-con-ventas');
      tabla.innerHTML = '';
      data.forEach(marca => {
        const fila = document.createElement('tr');
        fila.innerHTML = `<td>${marca.nombre}</td>`;
        tabla.appendChild(fila);
      });
    });
}

function cargarPrendasVendidas() {
  fetch('/api/v1/prendas_vendidas')
    .then(res => res.json())
    .then(data => {
      const tabla = document.getElementById('tabla-prendas-vendidas');
      tabla.innerHTML = '';
      data.forEach(prenda => {
        const fila = document.createElement('tr');
        fila.innerHTML = `
          <td>${prenda.nombre}</td>
          <td>${prenda.vendidas}</td>
          <td>${prenda.stock}</td>
        `;
        tabla.appendChild(fila);
      });
    });
}

function cargarTopMarcas() {
  fetch('/api/v1/top_marcas')
    .then(res => res.json())
    .then(data => {
      const tabla = document.getElementById('tabla-top-marcas');
      tabla.innerHTML = '';
      data.forEach(marca => {
        const fila = document.createElement('tr');
        fila.innerHTML = `
          <td>${marca.nombre}</td>
          <td>${marca.ventas}</td>
        `;
        tabla.appendChild(fila);
      });
    });
}
