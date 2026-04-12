import L from 'leaflet'
import green from './assets/marker-icon-green.png';
import red from './assets/marker-icon-red.png';
import blue from './assets/marker-icon-blue.png';
import shadow from './assets/marker-shadow.png';

class StatusIcon extends L.Icon {
  constructor(url: string) {
    super({
      iconUrl: url,
      shadowUrl: shadow,
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowSize: [41, 41]
    });
  }
}

export const greenIcon = new StatusIcon(green);
export const redIcon = new StatusIcon(red);
export const blueIcon = new StatusIcon(blue);