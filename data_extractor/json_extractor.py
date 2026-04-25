import math

import requests
import json
import pandas as pd 
import geopandas as gpd
from shapely.geometry import Point

def load_json_data(config):
    data = get_data(config)
    print(data)
    data_extractor_config = config["data_format_config"]
    path_to_array = data_extractor_config['path_to_array']
    
    data = get_nested_item(data, path_to_array)

    if 'parser' in config:
        data = config['parser'](data)

    rows = []
    for item in data:
        attrs = normalize_attr(get_nested_item(item, data_extractor_config["path_to_attributes"]))
        lat = get_nested_item(item, data_extractor_config["lat_path"])
        lng = get_nested_item(item, data_extractor_config["lng_path"])
        if not are_coordinates_valid(lat, lng):
            continue
        rows.append({
            **attrs,
            "location": Point(lng, lat)
        })

    df = pd.DataFrame(rows)
    gdf = gpd.GeoDataFrame(df, geometry="location", crs="EPSG:4326")
    return gdf

def get_data(config):
    url = config['url']
    if 'path' in config:
        return get_data_with_post(url, config['path'])
    return json.loads(requests.get(url).content)

def get_nested_item(json, path):
    item = json
    for i in path:
        item = item[i]
    return item

def get_data_with_post(url, path):
    with open(path + "/payload.json", "r", encoding="utf-8") as f:
        payload = json.load(f)
    
    with open(path + "/headers.json", "r", encoding="utf-8") as f:
        headers = json.load(f)

    response = requests.post(url, headers=headers, json=payload)

    response.raise_for_status()

    return response.json()

def normalize_attr(attrs):
    if isinstance(attrs, dict):
        return attrs
    elif isinstance(attrs, list):
        return {str(i): v for i, v in enumerate(attrs)}
    else:
        return {}
    
def are_coordinates_valid(lat, lng):
    try:
        c_lat = float(lat)
        C_lng = float(lng)
        return math.isfinite(c_lat) and math.isfinite(C_lng)
    except (TypeError, ValueError):
        return False