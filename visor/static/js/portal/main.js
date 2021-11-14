     var map = L.map('map').setView([-12.939947, -74.247891], 13);
     map.attributionControl.setPrefix(
         `Desarrollado por: <a href="https://www.linkedin.com/in/geofrancisco/" title="GeoSIG" "target=" _blank">Francisco Contreras &middot Rafael Vasquez </a>`
     );
     L.control.locate({
         locateOptions: {
             maxZoom: 19
         }
     }).addTo(map);
     map.createPane('pane_baseMap');
     map.getPane('pane_baseMap').style.zIndex = 0;
     var baseMapsatelital = L.tileLayer(
         'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
             pane: 'pane_baseMap',
             attribution: '&copy; <a href="">Google Earth</a>',
             subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
             opacity: 1.0,
             minZoom: 13,
             maxZoom: 28,
             minNativeZoom: 0,
             maxNativeZoom: 20
         });
     var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
         maxZoom: 19,
         attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
     });

     map.addLayer(OpenStreetMap_Mapnik)
     // POPUPS
     function pop_risk(feature, layer) {
         var popupContent = `<table class="table-sm table-dark table-bordered border-white">
        <thead>
            <tr>
                <th scope="col"> Manzana</th>
                <th scope="col">Distrito</th>
                <th scope="col">Poblacion</th>
                <th scope="col">Riesgo</th>

            </tr>
        </thead>
        <tbody>
            <tr>
                <td scope="row">${feature.properties.idmanzana}</td>
                <td class="fw-bolder">${feature.properties.distrito}</td>
                <td>${feature.properties.pob_total}</td>
                <td rowspan="2" class="">${feature.properties.n_riesgo}</td>
            </tr>
            <tr>
                <th scope="row" colspan="3"> Centro Poblado: ${feature.properties.nom_ccpp}</th>

            </tr>
        <tbody>
        </table>
        `;
         layer.bindPopup(popupContent, {
             maxHeight: 1000,
             maxWidth: 1000,

         });
     }

     function risk_stile(feature) {
         switch (String(feature.properties['n_riesgo'])) {
             case "Muy Alto":
                 return {
                     color: '#d7191c',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Alto":
                 return {
                     color: '#fe9000',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Medio":
                 return {
                     color: '#ffe900',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Bajo":
                 return {
                     color: '#1a9641',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
         }
     }

     function riskStile(feature) {
         switch (String(feature.properties['n_riesgo'])) {
             case "Muy Alto":
                 return {
                     color: '#d7191c',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Alto":
                 return {
                     color: '#fe9000',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Medio":
                 return {
                     color: '#ffe900',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
             case "Bajo":
                 return {
                     color: '#1a9641',
                         fillOpacity: '0.60',
                         stroke: ''
                 };
         }
     }

     // CREATE LAYERPANE
     map.createPane('dist_pane');
     map.getPane('dist_pane').style.zIndex = 400
     distritos = '{{data|safe}}'
     data = JSON.parse(distritos)
     var distritos_layer = new L.geoJson(data, {
         attribution: '',
         interactive: true,
         onEachFeature: pop_risk,
         pane: 'dist_pane',
         dataVar: 'distritos',
         layerName: 'Escenario de Riesgos',
         style: function (feature) {
             switch (String(feature.properties['n_riesgo'])) {
                 case "Muy Alto":
                     return {
                         color: '#d7191c',
                             fillOpacity: '0.60',
                             stroke: ''
                     };
                 case "Alto":
                     return {
                         color: '#fe9000',
                             fillOpacity: '0.60',
                             stroke: ''
                     };
                 case "Medio":
                     return {
                         color: '#ffe900',
                             fillOpacity: '0.60',
                             stroke: ''
                     };
                 case "Bajo":
                     return {
                         color: '#1a9641',
                             fillOpacity: '0.60',
                             stroke: ''
                     };
             }
         }


     }).addTo(map)

     var basemaps = {
         "Google Earth: ": baseMapsatelital,
         "OpenStreeMaps: ": OpenStreetMap_Mapnik
     };

     var theme = {
         "Escenario Riesgo Covid: ": distritos_layer
     }

     L.control.layers(basemaps, theme).addTo(map)
     var searchLayer = L.layerGroup().addTo(map);
     map.addControl(new L.Control.Search({
         url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
         jsonpParam: 'json_callback',
         propertyName: 'display_name',
         propertyLoc: ['lat', 'lon'],
         autoCollapse: true,
         autoType: false,
         minLength: 2,
         collapse: false

     }))