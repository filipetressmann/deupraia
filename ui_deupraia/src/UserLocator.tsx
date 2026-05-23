import { useEffect, useState } from 'react';
import { useMapEvents, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import { blueIcon } from './MapIcons';
import { useTranslation } from 'react-i18next';

function UserLocationMarker() {
    const [position, setPosition] = useState<L.LatLng | null>(null);
    const { t } = useTranslation();
    const map = useMap();

    useEffect(() => {
        map.locate({
            watch: true,
        });
    }, [map]);

    useMapEvents({
        locationfound(location) {
            setPosition(location.latlng);
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