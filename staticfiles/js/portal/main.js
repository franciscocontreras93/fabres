    var map = L.map('map', {
        drawControl: true
    }).setView([-12.939947, -74.247891], 13);

    map.attributionControl.setPrefix(
        `Desarrollado por: <a href="https://www.linkedin.com/in/geofrancisco/" title="GeoSIG" "target=" _blank">Francisco
        Contreras &middot Rafael Vasquez </a>`
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
    }).addTo(map);

    // map.addLayer(OpenStreetMap_Mapnik)
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


    // CREATE LAYERPANE
    map.createPane('dist_pane');
    map.getPane('dist_pane').style.zIndex = 400
    distritos = '{{data|safe}}'
    dist = '{{data2|safe}}'

    data = JSON.parse(distritos)

    var covid_riesgo_lyr = new L.geoJson(data, {
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

    map.fitBounds(covid_riesgo_lyr.getBounds());


    var dens_pob_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_densid'])) {
                case "Q5":
                    return {
                        color: '#440154',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q4":
                    return {
                        color: '#3a528b',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q3":
                    return {
                        color: '#20908d',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q2":
                    return {
                        color: '#5dc962',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q1":
                    return {
                        color: '#fde725',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
            }
        }


    })
    var pob_nbi_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_propnbi'])) {
                case "Q5":
                    return {
                        color: '#9f4f00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q4":
                    return {
                        color: '#db7909',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q3":
                    return {
                        color: '#e7a612',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q2":
                    return {
                        color: '#f3d31b',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case "Q1":
                    return {
                        color: '#ffff24',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
            }
        }


    })
    var nivel_contagio_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_mcalor'])) {
                case 'Q5':
                    return {
                        color: '#d7191c',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q4':
                    return {
                        color: '#d7191c',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q3':
                    return {
                        color: '#fea600',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q2':
                    return {
                        color: '#fea600',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q1':
                    return {
                        color: '#c7e800',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'N/D':
                    return {
                        color: '#c7e800',
                            fillOpacity: '0.60',
                            stroke: ''
                    };

            }
        }


    })
    var q30_59_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_30_a_59'])) {
                case 'Q5':
                    return {
                        color: '#d7191c',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q4':
                    return {
                        color: '#fd7a00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q3':
                    return {
                        color: '#ffff00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q2':
                    return {
                        color: '#abdd00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q1':
                    return {
                        color: '#1a9641',
                            fillOpacity: '0.60',
                            stroke: ''
                    };


            }
        }


    })
    var q60_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_pob60'])) {
                case 'Q5':
                    return {
                        color: '#d7191c',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q4':
                    return {
                        color: '#fd7a00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q3':
                    return {
                        color: '#ffff00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q2':
                    return {
                        color: '#abdd00',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q1':
                    return {
                        color: '#1a9641',
                            fillOpacity: '0.60',
                            stroke: ''
                    };


            }
        }


    })
    var qMercado_lyr = new L.geoJson(data, {
        attribution: '',
        interactive: true,
        onEachFeature: pop_risk,
        pane: 'dist_pane',
        dataVar: 'distritos',
        layerName: 'Escenario de Riesgos',
        style: function (feature) {
            switch (String(feature.properties['q_mercado'])) {
                case 'Q5':
                    return {
                        color: '#ff0000',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q4':
                    return {
                        color: '#ffa962',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q3':
                    return {
                        color: '#d5f23e',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q2':
                    return {
                        color: '#aef289',
                            fillOpacity: '0.60',
                            stroke: ''
                    };
                case 'Q1':
                    return {
                        color: '#bebebe',
                            fillOpacity: '0.60',
                            stroke: ''
                    };


            }
        }


    })





    var basemaps = {
        "Google Earth: ": baseMapsatelital,
        "OpenStreeMaps: ": OpenStreetMap_Mapnik
    };

    var theme = {
        "Escenario Riesgo Covid-19: ": covid_riesgo_lyr,
        "Densidad Poblacional: ": dens_pob_lyr,
        "Poblacion NBI: ": pob_nbi_lyr,
        "Areas de Contagio (EN DESARROLLO)": nivel_contagio_lyr,
        "Dist. Pob 30 a 59:": q30_59_lyr,
        "Dist. Mayores de 60:": q60_lyr,
        "Areas de Influencia Publica:": qMercado_lyr,

    }

    L.control.layers(basemaps, theme).addTo(map)

    // var sidebar = L.control.sidebar({ container: 'sidebar', position:'right'}).addTo(map);
    // console.log(covid_riesgo_lyr.getBounds())

    drawnItems = L.featureGroup().addTo(map);

    var drawControl = new L.Control.Draw({
        edit: {
            featureGroup: drawnItems
        }
    });
    map.addControl(drawControl);