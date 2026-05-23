import { useEffect, useRef } from "react";
import type { BeachData } from "./BeachData"
import { greenIcon, redIcon } from "./MapIcons";
import { useTranslation } from 'react-i18next';
import { Marker, Popup } from "react-leaflet";
import './styling/BeachMarker.css'

interface BeachMarkerProps {
    idx: number
    beach: BeachData
    selected: boolean
}

function BeachMarker(props: BeachMarkerProps) {
    const { t } = useTranslation();
    const markerRef = useRef<L.Marker>(null);

    useEffect(() => {
        if (props.selected) {
            markerRef.current?.openPopup();
        }
    }, [props.selected]);

    return <>
        <Marker 
            ref={markerRef}
            key={props.idx} 
            position={[props.beach.lat, props.beach.lng]}
            icon={getIcon(props.beach.status)}
        >
            <Popup>
                <div className="popup-content">
                    <h3>{props.beach.id}</h3>

                    <div className="popup-row">
                        <span className="label">
                            {t('last_updated')}
                        </span>

                        <span>
                            {props.beach.date}
                        </span>
                    </div>

                    <div className="popup-row">
                        <span className="label">
                            {t('result')}
                        </span>

                        <span
                            className={
                                props.beach.status === "PROPER"
                                    ? "status-proper"
                                    : "status-improper"
                            }
                        >
                            {t(props.beach.status)}
                        </span>
                    </div>
                </div>
            </Popup>
        </Marker>
    </>
}

const getIcon = (status: string) => {
  return status === 'PROPER' ? greenIcon : redIcon;
};

export default BeachMarker