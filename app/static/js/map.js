var ciudadesGeoJSON = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "nombre": "Tecnológico Cintalapa",
                "tipo": "PrimaryKey"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-93.74366340386732, 16.669932500845167]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "nombre": "Tecnológico Tuxtla Gutiérrez",
                "tipo": "PrimaryKey"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-93.17270474651072,16.757414581918116]
            }
        },
        // Agrega más ciudades aquí si es necesario
    ]
}

var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; OpenStreetMap contributors'
}).addTo(map);

// Crear la capa de GeoJSON
var ciudadesLayer = L.geoJSON(ciudadesGeoJSON);

var searchControl = new L.Control.Search({
    layer: L.geoJSON(ciudadesGeoJSON),
    propertyName: 'nombre',
    marker: false,
    moveToLocation: function(latlng, title, map) {
      var direccionBuscada = title; // Guardar la dirección buscada en una variable
      map.setView(latlng, 14); // Mantener el nivel de zoom actual del mapa
      // Realizar operaciones adicionales para asociar la dirección a un objeto en tu base de datos
      guardarDireccionEnBaseDeDatos(direccionBuscada);
    },
    autoCollapse: true
  }).addTo(map);

  function guardarDireccionEnBaseDeDatos(direccion) {
    var mensaje = 'Dirección guardada: ' + direccion;
    document.getElementById('mensaje-guardado').innerHTML = mensaje;
    
    // Aquí puedes escribir el código para guardar la dirección en tu base de datos
    // ...
    // Guardar la dirección en el localStorage
  localStorage.setItem('direccionGuardada', direccion);

  // Aquí puedes escribir el código para guardar la dirección en tu base de datos
  // ...
  }

  window.addEventListener('load', function() {
    // Obtener la dirección guardada del localStorage
    var direccionGuardada = localStorage.getItem('direccionGuardada');
  
    if (direccionGuardada) {
      var mensaje = 'Dirección guardada: ' + direccionGuardada;
      document.getElementById('mensaje-guardado').textContent = mensaje;
    }
  });










