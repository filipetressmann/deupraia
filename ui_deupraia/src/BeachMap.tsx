import { Marker, Popup, TileLayer } from "react-leaflet";
import { MapContainer } from "react-leaflet";
import Papa from 'papaparse';
import beachDataCSV from './assets/output.csv?raw';
import { useEffect, useState } from "react";
import type { LatLngExpression } from "leaflet";
import { useTranslation } from 'react-i18next';
import './i18n';
import { greenIcon, redIcon } from "./MapIcons";
import UserLocationMarker from "./UserLocator";

const center: LatLngExpression = [-23.0, -46.505]
const zoom = 6

interface BeachData {
  id: string;
  lat: string;
  lng: string;
  date: string;
  status: string;
}

function BeachMap() {
    const { t } = useTranslation();
    const [points, setPoints] = useState<BeachData[]>([]);

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
            <MapContainer 
                center={center} 
                zoom={zoom}
            >
                <TileLayer 
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                <UserLocationMarker />

                {points.map((point, idx) => (
                    <Marker 
                        key={idx} 
                        position={[parseFloat(point.lat), parseFloat(point.lng)]}
                        icon={getIcon(point.status)}
                    >
                        <Popup>
                            {t('beach_name')}: <strong>{point.id}</strong><br />
                            {t('last_updated')}: {point.date}<br />
                            {t('result')}: {t(point.status)}
                        </Popup>
                  </Marker>
                ))}
            </MapContainer>
        </>
    )
}

const getIcon = (status: string) => {
  return status === 'PROPER' ? greenIcon : redIcon;
};

export default BeachMap;