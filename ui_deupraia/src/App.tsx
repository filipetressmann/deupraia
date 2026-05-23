import type { BeachData } from './BeachData';
import Papa from 'papaparse';
import beachDataCSV from './assets/output.csv?raw';
import { useEffect, useState } from "react";
import BeachMap from './BeachMap';
import { type LatLngExpression } from 'leaflet';
import SearchBar from './SearchBar';
import './styling/App.css';

function App() {

  const [center, setCenter] = useState<LatLngExpression>();
  const [points, setPoints] = useState<BeachData[]>([]);
  const [selectedBeach, setSelectedBeach] = useState<string>()

  useEffect(() => {
    Papa.parse(beachDataCSV, {
        header: true,
        skipEmptyLines: true,
        complete: (results) => {
            setPoints(results.data as BeachData[]);
        },
    });
  }, []);

  return (
    <div className="app-wrapper">
      <SearchBar 
        beaches={points} 
        setCenter={setCenter}
        setSelectedBeach={setSelectedBeach}
      />
      <BeachMap 
        points={points} 
        center={center}
        selectedBeach={selectedBeach}
      />
    </div>
  )
}

export default App;
