
import React, { Component }  from 'react';
import { useAsync, IfPending, IfFulfilled, IfRejected } from "react-async"
import { MapContainer, GeoJSON, Popup, TileLayer } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
import tileLayer from './tileLayer';

const loadMap = async () => {
    const result = await fetch(`http://localhost:8000/map/`)
    if (!result.ok) throw new Error(result.statusText)
    return result.json()
}

const onEachPolygon = (polygon, layer) => {
  const power = (parseFloat(polygon.properties.Output_kwh))/1000;
  layer.bindPopup(String(power) + ' MWh Annual');

};

// Asynchronous fetching of data, using react-async declarative components for clarity
// Use https://blog.bitsrc.io/declarative-data-fetching-with-react-async-d4dfc63b0597 as a template
            {/* onEachFeature={this.onEachPolygon} */}
const SolarMap = () => {
  const state = useAsync({ 
    promiseFn: loadMap,
  });
  return (
    <div>
      <IfPending state={state}>Loading...</IfPending>
      <IfRejected state={state}>{error => `Something went wrong: ${error.message}`}</IfRejected>
      <IfFulfilled state={state}>
        <div id="map">
        <MapContainer center={[54.66395, -2.75230]} zoom={16}>
          <TileLayer {...tileLayer} />
          <GeoJSON 
            data={state.data} onEachFeature={onEachPolygon} />
        </MapContainer>
        </div>  
      </IfFulfilled>
    </div>
  )
}
export default SolarMap;