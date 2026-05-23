import { TileLayer, MapContainer, useMap } from "react-leaflet";
import type { LatLngExpression } from "leaflet";
import './i18n';
import UserLocationMarker from "./UserLocator";
import type { BeachData } from "./BeachData";
import { useEffect } from "react";
import BeachMarker from "./BeachMarker";

const defaultCenter: LatLngExpression = [-23.0, -46.505]
const zoom = 6

interface BeachMapProps {
    points: BeachData[]
    center: LatLngExpression | undefined
    selectedBeach: string | undefined
}

interface MapControllerProps {
    center: LatLngExpression | undefined
}

function MapController(props: MapControllerProps) {
    const map = useMap();

    useEffect(() => {
        const center = props.center ?? defaultCenter
        if (props.center) {
            map.flyTo(center, 14)
        }
    }, [props.center, map]);

    return null;
}

function BeachMap(props: BeachMapProps) {
    return (
        <>
            <MapContainer 
                center={props.center ?? defaultCenter} 
                zoom={zoom}
            >
                <TileLayer 
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                <UserLocationMarker />

                <MapController center={props.center}/>

                {props.points.map((point, idx) => (
                    <BeachMarker 
                        idx={idx} 
                        beach={point}
                        selected={point.id == props.selectedBeach}
                    />
                ))}
            </MapContainer>
        </>
    )
}

export default BeachMap;