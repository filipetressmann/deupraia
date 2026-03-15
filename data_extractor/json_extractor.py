import requests
import json
import pandas as pd 
import geopandas as gpd
from shapely.geometry import Point

def load_json_data(config):
    url = config['url']
    data = json.loads(requests.get(url).content)
    data_extractor_config = config["data_format_config"]
    path_to_array = data_extractor_config['path_to_array']
    
    data = get_nested_item(data, path_to_array)

    rows = []
    for item in data:
        attrs = get_nested_item(item, data_extractor_config["path_to_attributes"])
        lat = get_nested_item(item, data_extractor_config["lat_path"])
        lng = get_nested_item(item, data_extractor_config["lng_path"])

        rows.append({
            **attrs,
            "location": Point(lng, lat)
        })

    df = pd.DataFrame(rows)

    gdf = gpd.GeoDataFrame(df, geometry="location", crs="EPSG:4326")
    return gdf

def get_nested_item(json, path):
    item = json
    for i in path:
        item = item[i]
    
    return item