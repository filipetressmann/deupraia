import { useEffect, useState } from 'react';
import { useMapEvents, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import { blueIcon } from './MapIcons';
import { useTranslation } from 'react-i18next';

function UserLocationMarker() {
    const [position, setPosition] = useState<L.LatLng | null>(null);
    const { t } = useTranslation();
    const map = useMap();

    // 1. Move the locate call into useEffect with an empty dependency array
    useEffect(() => {
        map.locate({
            watch: true,
        });
    }, [map]); // Runs only once when the map instance is ready

    useMapEvents({
        locationfound(location) {
            if (!position) {
                setPosition(location.latlng);
                map.setView(location.latlng, 13);
            }
        },
        locationerror() {
            console.log("Location access denied.");
        }
    });

    return position === null ? null : (
        <Marker 
            position={position}
            icon={blueIcon}
        >
            <Popup>{t('user_location')}</Popup>
        </Marker>
    );
}

export default UserLocationMarker;