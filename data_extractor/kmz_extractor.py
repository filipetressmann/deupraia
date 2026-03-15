import requests

import pandas as pd 
import geopandas as gpd

filename = 'kmz_file.kmz'
pd.set_option('display.max_columns', None)

def load_kmz_data(config):
    url = config['url']
    kmz_file_compressed = requests.get(url).content
    with open(filename, "wb") as text_file:
        text_file.write(kmz_file_compressed)
    
    data_extractor_config = config["data_format_config"]
    df = None
    if data_extractor_config['layers'] is not None:
        layers = [gpd.read_file(filename, layer=l) for l in data_extractor_config['layers']]
        df = pd.concat(layers)
    else:
        df = gpd.read_file(filename)

    return df[data_extractor_config["columns"]].dropna()
