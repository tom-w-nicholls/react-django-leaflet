import React from 'react';
// import logo from './logo.svg';
// import axios from 'axios';
// As a more sophisticated alternative to AXIOS, try using SWR:
// https://www.smashingmagazine.com/2020/06/introduction-swr-react-hooks-remote-data-fetching/
import './App.css';
import SolarMap from './solarmap';
// import MapWrapper from './geoJson-simple-example-not-mine';

function App() {
  return (
    <div className="App">
      <SolarMap/>   
    </div>
  );
}

export default App;
