import type { BeachData } from './BeachData';
import Papa from 'papaparse';
import beachDataCSV from './assets/output.csv?raw';
import { useEffect, useState } from "react";
import BeachMap from './BeachMap';
import { type LatLngExpression } from 'leaflet';
import SearchBar from './SearchBar';
import './styling/App.css';
import { Helmet } from 'react-helmet-async'

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
    <>
      <Helmet>
        <title>
          Brazil Beach Water Quality Map
        </title>

        <meta
          name="description"
          content="
            Mapa de balneabilidade das praias do Brasil. Este mapa possui dados
            das praias do Rio de Janeiro, São Paulo, Santa Catarina e Espirito Santo."
        />

        <meta
          name="keywords"
          content="
            qualidade das aguas das praias do brasil, 
            praias brasileiras, balneabilidade das praias, 
            praias limpas"
        />

        <meta
          property="og:title"
          content="Mapa de Balneabilidade das Praias do Brasil"
        />

        <meta
          property="og:description"
          content="Consulte a qualidade da água e as condições de banho das praias brasileiras."
        />
        <meta
          property="og:type"
          content="website"
        />
      </Helmet>
      <main className="app-wrapper">
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
      </main>
    </>
  )
}

export default App;
