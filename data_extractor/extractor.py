import pandas as pd 
import sys

from extractor_config import CONFIG, TEST_CONFIG
from json_extractor import load_json_data
from kmz_extractor import load_kmz_data
from shapely.geometry import Point, mapping

format_mapping = {
    'kmz': load_kmz_data,
    'json': load_json_data
}

# Sao Paulo https://arcgis.cetesb.sp.gov.br/server/rest/services/Hosted/Praias/FeatureServer/0/query?where=1%3D1&fullText=&objectIds=&uniqueIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=praia%2Cdata_amostra_inicio%2Cclassificacao_texto&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&datumTransformation=&lodType=geohash&lod=&lodSR=&cacheHint=false&returnUniqueIdsOnly=false&f=pjson

def load_data(config):
    format = config['format']
    return format_mapping[format](config)

def get_data_for_config(config):
    try:
        df = load_data(config)

        transforms = config["transforms"]

        for transform in transforms:
            df = transform["function"](df, transform)

        mappings = config["mappings"]
        
        df = (
            df[list(mappings.keys())]
                .rename(columns=mappings)
        )

        df['id'] = config['disambiguator']+ ' ' +  df['id'].astype(str)
        df["location"] = df.location.apply(
            lambda geom: Point(geom.x, geom.y)
        )

        df["status"] = df["status"].map(config['status_mapping'])
        return df
    except Exception as e:
        print("Failed for config: ", config)
        print("Error: ", e)
        raise e


if __name__ == "__main__":
    is_test = len(sys.argv) > 1
    configs = CONFIG
    if is_test:
        configs = TEST_CONFIG
    df = pd.concat([get_data_for_config(config) for config in configs])
    print(df.head(1000))
