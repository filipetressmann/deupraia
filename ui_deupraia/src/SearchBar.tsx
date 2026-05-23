import Select from "react-select";
import type { BeachData } from "./BeachData";
import type { Dispatch, SetStateAction } from "react";
import type { LatLngExpression } from "leaflet";
import './styling/SearchBar.css';

interface SearchBarProps {
    beaches: BeachData[]
    setCenter: Dispatch<SetStateAction<LatLngExpression | undefined>>
    setSelectedBeach: Dispatch<SetStateAction<string | undefined>>
}

type OptionType = {
    label: string
    value: [number, number]
}

function SearchBar(props: SearchBarProps) {
    const values: OptionType[] = props.beaches.map((value) => ({
        label: value.id,
        value: [
            value.lat,
            value.lng,
        ],
    }))

    return (
        <div className="search-bar">
            <Select<OptionType>
                options={values}
                onChange={(newValue) => {
                    if (!newValue) return
                    props.setCenter(newValue.value)
                    props.setSelectedBeach(newValue.label)
                }}
            />
        </div>
    )
}

export default SearchBar;